import numpy as np
from abc import ABC, abstractmethod
from typing import Callable, override

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

