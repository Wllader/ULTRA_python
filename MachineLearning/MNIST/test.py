from misc.misc import get_data, FileType
from misc.recognizers import *
import numpy as np



X_train = get_data(FileType.TrainImage)
y_train = get_data(FileType.TrainLabel)

X_test = get_data(FileType.TestImage)
y_test = get_data(FileType.TestLabel)


mlp = MultilayerPerceptronRecognizer(
    X_train,
    y_train,
    (16, 16),
    batch_size=8,
    seed=42,
    train_bias=False
)

print(
    mlp.predict(X_test[0]),
    y_test[0]
)

print(
    mlp.score(X_test, y_test)
)