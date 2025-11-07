from misc.misc import get_data, FileType
from misc.recognizers import *
import numpy as np



X_train = get_data(FileType.TrainImage)
y_train = get_data(FileType.TrainLabel)

X_test = get_data(FileType.TestImage)
y_test = get_data(FileType.TestLabel)


mlp = MulticlassLogisticRegressionRecognizer(X_train, y_train, epochs=10, train_bias=True, seed=42)

print(
    mlp.predict(X_test[0]),
    y_test[0]
)

print(
    mlp.score(X_test, y_test)
)