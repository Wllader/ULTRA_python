import numpy as np
from abc import ABC, abstractmethod
from typing import Callable, override

class Activations:
    @staticmethod
    def softmax(x:np.ndarray) -> np.ndarray:
        _x:np.ndarray = x - x.max()
        _x = np.exp(_x)
        return _x / np.sum(_x, axis=1, keepdims=1)


class RecognizerStrategy(ABC):
    def __init__(self, X_train:np.ndarray, y_train:np.ndarray, normalize=True):
        super().__init__()

    @abstractmethod
    def predict(self, image:np.ndarray) -> np.ndarray:
        pass

    def _add_bias(self, A:np.ndarray) -> np.ndarray:
        if not self.train_bias:
            return A
        
        return np.pad(A, [(0, 0), (0, 1)], constant_values=1)


class AverageDistanceRecognizer(RecognizerStrategy):
    def __init__(self, X_train:np.ndarray, y_train:np.ndarray, normalize=True):
        super().__init__(X_train, y_train)

        self.normalize = normalize
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
            img = image/255.
        else:
            img = image.copy()

        scores = (self.averages * img).sum(axis=(1, 2))

        scores -= scores.min()
        if scores.max() > 0:
            scores /= scores.max()

        return scores


class CosineSimilarityRecognizer(RecognizerStrategy):
    def __init__(self, X_train:np.ndarray, y_train:np.ndarray, normalize=True, temperature:float=1.0):
        super().__init__(X_train, y_train, normalize)

        self.normalize = normalize
        self.temp = temperature

        X_train = X_train.astype(np.float32)
        if self.normalize:
            X_train /= 255.

        self.averages = np.array([
            X_train[(y_train == n).flatten()].mean(axis=0)
            for n in range(10)
        ], dtype=np.float32)

        self.flat_averages = self.averages.reshape(10, -1)
        self.avg_norms = np.linalg.norm(self.flat_averages, axis=1) + 1e-8

    def predict(self, image:np.ndarray) -> np.ndarray:
        img = image.astype(np.float32)
        if self.normalize:
            img /= 255.

        flat = img.flatten()
        img_norm = np.linalg.norm(flat) + 1e-8


        cos_sim = (self.flat_averages @ flat) / (self.avg_norms * img_norm)

        logits = cos_sim / self.temp
        logits -= logits.max()
        exp_logits = np.exp(logits)

        scores = exp_logits - exp_logits.min()
        scores /= scores.max()

        return scores if scores.max() > 0 else np.zeros(10)

class MulticlassLogisticRegression(RecognizerStrategy):
    def __init__(self, X_train:np.ndarray, y_train:np.ndarray, epoch:int=10, batch_size:int=10, train_bias=True, seed=None):
        super().__init__(X_train, y_train, True)
        self.train_bias = train_bias

        generator = np.random.RandomState(seed=seed)
        N = X_train.shape[0]

        X_train = X_train.astype(np.float32)
        X_train = X_train.reshape([N, -1])
        X_train /= 255.

        X_train = self._add_bias(X_train)

        D = X_train.shape[1]
        K = 10

        y_train_ohe = np.eye(y_train.max() + 1, dtype=bool)[y_train]

        B = batch_size
        alpha = .01

        self.weights = np.zeros((D, K), dtype=np.float64)

        e = 0
        while e < epoch:
            permutation = generator.permutation(X_train.shape[0])
            for batch_index in range(N//B):
                _start, _stop = np.array([batch_index, batch_index+1]) * B
                idx = permutation[_start:_stop]

                X_ = X_train[idx]
                t_ = y_train_ohe[idx]

                g = X_.T @ (Activations.softmax(X_ @ self.weights) - t_)
                self.weights -= alpha * g/B
            
            e += 1

    def predict(self, X:np.ndarray, normalize:bool = True):
        X_ = np.reshape(X, X.shape[0] * X.shape[1], copy=True)
        X_ = X_ / X_.max()

        if self.train_bias:
            X_ = np.pad(X_, [(0, 1)], constant_values=1)

        scores = X_ @ self.weights
        if normalize:
            scores -= scores.min()
            scores /= scores.max()

        return scores if scores.max() > 0 else np.zeros_like(scores)







