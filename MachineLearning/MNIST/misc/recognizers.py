import numpy as np
from abc import ABC, abstractmethod
from typing import Callable


class Activations:
    @staticmethod
    def ReLU(x:np.ndarray):
        return np.where(x > 0, x, 0)
    
    @staticmethod
    def ReLU_grad(x:np.ndarray):
        return (x > 0).astype(float)
    
    @staticmethod
    def softmax(x:np.ndarray) -> np.ndarray:
        _x:np.ndarray = x - x.max()
        _x = np.exp(_x)
        return   _x / np.sum(_x, axis=1, keepdims=1)

    

class RecognizerStrategy(ABC):
    """Abstract interface for number recognition strategies."""

    @abstractmethod
    def predict(self, image: np.ndarray) -> np.ndarray:
        """Return normalized output vector of shape (10,)."""
        pass

    def _add_bias(self, A:np.ndarray) -> np.ndarray:
        """Add bias column if enabled"""
        if not self.train_bias:
            return A
        
        return np.pad(A, [(0, 0), (0, 1)], constant_values=1)



class AverageDistanceRecognizer(RecognizerStrategy):
    """
    A naive recognizer that compares an input image to
    the average of each digit class using dot product similarity.
    """

    def __init__(self, X_train: np.ndarray, y_train: np.ndarray, normalize=True):
        """
        Args:
            X_train: training images (N, H, W)
            y_train: labels (N,)
            normalize: whether to normalize image intensities to [0, 1]
        """
        self.normalize = normalize
        if self.normalize:
            X_train = X_train.astype(np.float32)
            X_train /= 255.0

        # compute class averages
        self.averages = np.array([
            X_train[(y_train == n).flatten()].mean(axis=0)
            for n in range(10)
        ], dtype=np.float32)

    # ------------------------------------------------------------
    def predict(self, image: np.ndarray) -> np.ndarray:
        """Return normalized similarity vector for the given image."""
        img = image.astype(np.float32)
        if self.normalize:
            img /= 255.0

        # similarity to each average (dot product)
        scores = (self.averages * img).sum(axis=(1, 2))

        # normalize to [0,1] (like a pseudo-probability)
        scores -= scores.min()
        if scores.max() > 0:
            scores /= scores.max()

        return scores


class CosineSimilarityRecognizer(RecognizerStrategy):
    """
    Recognizer that compares input image to class averages
    using cosine similarity, returning softmax-normalized probabilities.
    """

    def __init__(self, X_train: np.ndarray, y_train: np.ndarray, normalize=True, temperature: float = 1.0):
        """
        Args:
            X_train: training images (N, H, W)
            y_train: labels (N,)
            normalize: whether to scale input images to [0,1]
            temperature: controls softmax sharpness (smaller = more confident)
        """
        self.normalize = normalize
        self.temperature = temperature

        X_train = X_train.astype(np.float32)
        if normalize:
            X_train /= 255.0

        # Compute class averages
        self.averages = np.array([
            X_train[(y_train == n).flatten()].mean(axis=0)
            for n in range(10)
        ], dtype=np.float32)

        # Precompute norms
        self.flat_averages = self.averages.reshape(10, -1)
        self.avg_norms = np.linalg.norm(self.flat_averages, axis=1) + 1e-8

    def predict(self, image: np.ndarray) -> np.ndarray:
        """Return normalized probability vector (softmax of cosine similarities)."""
        img = image.astype(np.float32)
        if self.normalize:
            img /= 255.0
        flat = img.flatten()
        img_norm = np.linalg.norm(flat) + 1e-8

        # Cosine similarity with each class average
        cos_sim = (self.flat_averages @ flat) / (self.avg_norms * img_norm)

        # Temperature-scaled softmax
        logits = cos_sim / self.temperature
        logits -= np.max(logits)  # softmax stability
        exp_logits = np.exp(logits)

        scores = exp_logits - exp_logits.min()
        scores /= scores.max()

        return scores if scores.max() > 0 else np.zeros(10)
    

class MulticlassLogisticRegressionRecognizer(RecognizerStrategy):
    def __init__(self, X_train:np.ndarray, y_train:np.ndarray, epochs:int=10, batch_size:int=10, train_bias=True, seed=None):
        super().__init__()
        self.train_bias = train_bias

        generator = np.random.RandomState(seed=seed)
        N = X_train.shape[0]

        X_train_ = X_train.reshape([N, -1])
        X_train_ = X_train_ / X_train_.max()

        X_train_ = self._add_bias(X_train_)

        D = X_train_.shape[1]
        K = 10

        y_train_ohe = np.eye(y_train.max() + 1, dtype=bool)[y_train]

        B = batch_size

        alpha = 0.01

        self.weights = np.zeros((D, K), dtype=np.float64)

        e = 0
        early_stop = False
        while e < epochs and not early_stop:
            permutation = generator.permutation(X_train_.shape[0])

            for batch_index in range(N//B):
                _start, _stop = np.array([batch_index, batch_index+1]) * B
                
                X_ = X_train_[permutation[_start:_stop]]
                t_ = y_train_ohe[permutation[_start:_stop]]


                g = X_.T @ (Activations.softmax(X_ @ self.weights) - t_)

                self.weights -= alpha* g/B
            
            e += 1


    def predict(self, X: np.ndarray, normalize:bool = True):
        X_ = np.reshape(X, X.shape[0] * X.shape[1], copy=True)
        X_ = X_ / X_.max()

        if self.train_bias:
            X_ = np.pad(X_, [(0, 1)], constant_values=1)

        scores = X_ @ self.weights
        if normalize:
            scores -= scores.min()
            scores /= scores.max()

        return scores if scores.max() > 0 else np.zeros_like(scores)

    def score(self, X:np.ndarray, y:np.ndarray):
        X_:np.ndarray = np.reshape(X, [X.shape[0], -1], copy=True)
        X_ = X_ / X_.max()
        if self.train_bias:
            X_ = np.pad(X_, [(0, 0), (0, 1)], constant_values=1)

        y_pred = (X_ @ self.weights).argmax(axis=1) == y
        return y_pred.sum() / len(y)



class MultilayerPerceptronRecognizer(RecognizerStrategy):
    def __init__(self,
                 X_train: np.ndarray,
                 y_train: np.ndarray,
                 hidden_layers: tuple[int] = (128,),
                 epochs: int = 10,
                 batch_size: int = 32,
                 learning_rate: float = 0.01,
                 activation: tuple[Callable, Callable] = (Activations.ReLU, Activations.ReLU_grad),
                 train_bias: bool = True,
                 seed: int | None = None):
        """
        Args:
            X_train: (N, 28, 28) training images
            y_train: (N,) labels 0–9
            hidden_layers: tuple of hidden layer sizes
            epochs: number of epochs
            batch_size: mini-batch size
            learning_rate: learning rate
            activation: tuple of (f, f_grad) activation functions
            train_bias: whether to append bias units
            seed: random seed
        """
        super().__init__()
        self.train_bias = train_bias
        self.learning_rate = learning_rate
        generator = np.random.RandomState(seed)
        N = X_train.shape[0]

        # Normalize input
        X_train = X_train.reshape(N, -1).astype(np.float64)
        X_train /= X_train.max()

        # X_train = self._add_bias(X_train)

        D = X_train.shape[1]
        K = int(y_train.max()) + 1
        y_onehot = np.eye(K, dtype=np.float64)[y_train]

        self.act, self.act_grad = activation

        # Architecture
        layers = [X_train.shape[1], *hidden_layers, K]
        self.weights = []

        for i in range(len(layers) - 1):
            fan_in = layers[i] + (1 if self.train_bias else 0)
            fan_out = layers[i + 1]
            limit = np.sqrt(2 / fan_in)
            W = generator.uniform(-limit, limit, (fan_in, fan_out))
            self.weights.append(W)

        # Training
        B = batch_size
        for epoch in range(epochs):
            perm = generator.permutation(N)
            for i in range(0, N, B):
                idx = perm[i:i + B]
                Xb = X_train[idx]
                yb = y_onehot[idx]

                activations, preacts = self._forward(Xb)
                grads = self._backward(Xb, yb, activations, preacts)

                for j in range(len(self.weights)):
                    self.weights[j] -= self.learning_rate * grads[j] / B

    # ------------------------------------------------------------
    # Core network operations
    # ------------------------------------------------------------
    def _forward(self, X: np.ndarray):
        # X: (B, D) without bias
        activations = [X]
        preacts = []

        # hidden layers
        for W in self.weights[:-1]:
            A = self._add_bias(activations[-1])  # (B, in+1)
            Z = A @ W                            # (B, out)
            preacts.append(Z)
            A = self.act(Z)
            activations.append(A)

        # output layer
        A = self._add_bias(activations[-1])
        Z = A @ self.weights[-1]
        preacts.append(Z)
        activations.append(Activations.softmax(Z))

        return activations, preacts

    

    def _backward(self, X, y_true, activations, preacts):
        grads = [None] * len(self.weights)
        delta = activations[-1] - y_true  # dL/dZ for softmax

        for i in reversed(range(len(self.weights))):
            A_prev = activations[i]
            grads[i] = self._add_bias(A_prev).T @ delta

            if i > 0:
                Z_prev = preacts[i - 1]
                delta = delta @ self.weights[i].T
                if self.train_bias:
                    delta = delta[:, :-1]
                delta *= self.act_grad(Z_prev)
        return grads

    # ------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------
    def predict(self, X: np.ndarray, normalize: bool = True):
        X_ = X.reshape(1, -1).astype(np.float64)  # single image
        if normalize:
            X_ /= X_.max()

        A = X_
        for W in self.weights[:-1]:
            A = self.act(self._add_bias(A) @ W)
        Z = self._add_bias(A) @ self.weights[-1]
        probs = Activations.softmax(Z)
        return probs.ravel()

    def score(self, X: np.ndarray, y: np.ndarray):
        X_ = X.reshape([X.shape[0], -1]).astype(np.float64)
        X_ /= X_.max()
        y_pred = Activations.softmax(self._forward(X_)[0][-1]).argmax(axis=1)
        return (y_pred == y).mean()
