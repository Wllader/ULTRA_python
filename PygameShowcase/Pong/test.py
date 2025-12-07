import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([10, 20])
d = np.array([30, 40])


A = np.array((a-c, c-d)).T

print(a == (1, 2) or b == (3, 4))

