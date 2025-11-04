import numpy as np
from abc import ABC, abstractmethod


class RecognizerStrategy(ABC):
    """Abstract interface for number recognition strategies."""

    @abstractmethod
    def predict(self, image: np.ndarray) -> np.ndarray:
        """Return normalized output vector of shape (10,)."""
        pass


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

    # ------------------------------------------------------------
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