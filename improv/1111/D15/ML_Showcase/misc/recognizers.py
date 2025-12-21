import numpy as np
from abc import ABC, abstractmethod
from typing import Callable, override

class Activations:
    @staticmethod
    def softmax(x:np.ndarray) -> np.ndarray:
        _x:np.ndarray = x - x.max()
        _x = np.exp(_x)
        return _x / np.sum(_x, axis=1, keepdims=1)
    
    @staticmethod
    def ReLU(x:np.ndarray) -> np.ndarray:
        return np.where(x > 0, x, 0)
    
    @staticmethod
    def ReLU_grad(x:np.ndarray) -> np.ndarray:
        return (x > 0).astype(np.float32)

class RecognizerStrategy(ABC):
    def __init__(self, X_train:np.ndarray, y_train:np.ndarray, normalize=True):
        super().__init__()

        self.normalize = normalize

    @abstractmethod
    def predict(self, image:np.ndarray) -> np.ndarray:
        pass

    def _add_bias(self, A:np.ndarray) -> np.ndarray:
        if not self.train_bias:
            return A
        
        return np.pad(A, [(0, 0), (0, 1)], constant_values=1)
    
class AverageDistanceRecognizer(RecognizerStrategy):
    def __init__(self, X_train, y_train, normalize=True):
        super().__init__(X_train, y_train, normalize)

        X_train = X_train.astype(np.float32)
        if self.normalize:
            X_train /= 255.

        self.averages = np.array([
            X_train[(y_train == n).flatten()].mean(axis=0)
            for n in range(10)
        ], dtype=np.float32)

    @override
    def predict(self, image:np.ndarray) -> np.ndarray:
        if self.normalize:
            img = image / 255.
        else:
            img = image.copy()

        scores:np.ndarray = (self.averages * img).sum(axis=(1, 2))

        scores -= scores.min()
        if scores.max() > 0:
            scores /= scores.max()

        return scores
    
class CosineSimilarityRecognizer(RecognizerStrategy):
    def __init__(self, X_train, y_train, normalize=True, temperature:float=1.):
        super().__init__(X_train, y_train, normalize)

        self.tempr = temperature
        X_train = X_train.astype(np.float32)
        if self.normalize:
            X_train /= 255.

        self.averages = np.array([
            X_train[(y_train == n).flatten()].mean(axis=0)
            for n in range(10)
        ], dtype=np.float32)

        self.flat_averages = self.averages.reshape(10, -1)
        self.avg_norms = np.linalg.norm(self.flat_averages, axis=1) + 1e-8

    def predict(self, image):
        img = image.astype(np.float32)
        if self.normalize:
            img /= 255.

        flat = img.flatten()
        img_norm = np.linalg.norm(flat) + 1e-8

        cos_sim = (self.flat_averages @ flat) / (self.avg_norms * img_norm)

        logits:np.ndarray = cos_sim / self.tempr
        logits -= logits.max()
        exp_logits = np.exp(logits)

        scores = exp_logits - exp_logits.min()
        scores /= scores.max()

        return scores if scores.max() > 0 else np.zeros(10)
    

class MulticlassLogisticRegression(RecognizerStrategy):
    def __init__(self, X_train:np.ndarray, y_train:np.ndarray, epoch:int=10, batch_size:int=10, train_bias=True, seed=None):
        super().__init__(X_train, y_train, True)

        generator = np.random.RandomState(seed=seed)
        N = X_train.shape[0]

        X_train = X_train.astype(np.float32)
        X_train = X_train.reshape([N, -1])
        X_train /= 255.

        self.train_bias = train_bias
        if self.train_bias:
            X_train = self._add_bias(X_train)

        D = X_train.shape[1]
        K = 10

        y_train_ohe = np.eye(y_train.max() + 1, dtype=bool)[y_train]

        B = batch_size
        alpha = .01

        self.weights = np.zeros((D, K), dtype=np.float64)

        e = 0
        while e < epoch:
            permutation = generator.permutation(N)
            for batch_index in range(N//B):
                _start, _stop = np.array([batch_index, batch_index+1]) * B
                idx = permutation[_start:_stop]

                X_ = X_train[idx]
                t_ = y_train_ohe[idx]

                g = X_.T @ (Activations.softmax(X_ @ self.weights) - t_)
                self.weights -= alpha * g/B

            e += 1

    def predict(self, X:np.ndarray, normalize:bool=True):
        X_ = np.reshape(X, X.shape[0] * X.shape[1], copy=True)
        X_ = X_ / 255.

        if self.train_bias:
            X_ = np.pad(X_, [(0, 1)], constant_values=1)

        scores = X_ @ self.weights
        if normalize:
            scores -= scores.min()
            scores /= scores.max()

        return scores if scores.max() > 0 else np.zeros_like(scores)


class MultilayerPerceptronRecognizer(RecognizerStrategy):
    def __init__(
            self,
            X_train:np.ndarray,
            y_train:np.ndarray,
            hidden_layers: tuple[int] = (16, 16),
            epochs: int = 10,
            batch_size: int = 32,
            learning_rate: float = .01,
            activation: tuple[Callable] = (Activations.ReLU, Activations.ReLU_grad),
            train_bias: bool = True,
            seed: int | None = None
    ):
        super().__init__(X_train, y_train, True)

        self.train_bias = train_bias
        self.alpha = learning_rate
        generator = np.random.RandomState(seed)
        N = X_train.shape[0]

        X_train = X_train.reshape(N, -1).astype(np.float64)
        X_train /= 255.

        D = X_train.shape[1]
        K = int(y_train.max()) + 1
        y_onehot = np.eye(K, dtype=np.float64)[y_train]

        self.act, self.act_grad = activation

        layers = [X_train.shape[1], *hidden_layers, K]
        self.weights = []

        for i in range(len(layers) - 1):
            fan_in = layers[i] + self.train_bias
            fan_out = layers[i + 1]
            limit = np.sqrt(2 / fan_in)

            W = generator.uniform(-limit, limit, (fan_in, fan_out))
            self.weights.append(W)

        B = batch_size
        for _epoch in range(epochs):
            perm = generator.permutation(N)
            for i in range(0, N, B):
                idx = perm[i:i+B]

                X_ = X_train[idx]
                t_ = y_onehot[idx]

                activations, preacts = self._forward(X_)
                grads = self._backward(X_, t_, activations, preacts)

                for j in range(len(self.weights)):
                    self.weights[j] -= self.alpha * grads[j] / B

    def _forward(self, X:np.ndarray):
        activations = [X]
        preacts = []

        #hidden layers
        for W in self.weights[:-1]:
            A = self._add_bias(activations[-1])
            Z = A @ W
            preacts.append(Z)

            A = self.act(Z)
            activations.append(A)

        #output layer
        A = self._add_bias(activations[-1])
        Z = A @ self.weights[-1]
        preacts.append(Z)
        activations.append(Activations.softmax(Z))

        return activations, preacts
        
    def _backward(self, X, y_true, activations, preacts):
        grads = [ None for i in range(len(self.weights)) ]
        delta = activations[-1] - y_true

        for i in reversed(range(len(self.weights))):
            A_prev = activations[i]
            grads[i] = self._add_bias(A_prev).T @ delta

            if i > 0:
                Z_prev = preacts[i-1]
                delta = delta @ self.weights[i].T
                if self.train_bias:
                    delta = delta[:, :-1]

                delta *= self.act_grad(Z_prev)

        return grads
    
    def predict(self, X:np.ndarray, normalize:bool=True):
        X_ = X.reshape(1, -1).astype(np.float64)
        if normalize:
            X_ /= X_.max()

        for W in self.weights[:-1]:
            X_ = self.act(self._add_bias(X_) @ W)

        Z = self._add_bias(X_) @ self.weights[-1]
        scores = Activations.softmax(Z)

        return scores.ravel() 