import numpy as np

a = np.array([1, 0, 1])

# print(a)
# print(a[:, None])
# print(a[:, None].T)

# print(a+3)
# print(a*3)
# print(a//3)

b = np.array([1, 2, 3])

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)


# print(a@b)
# print(b@a)
# print(np.dot(a, b))


M = np.array([[1, 1, 1], [1, 1, 1]])
N = np.array([[1, 2, 3], [4, 5, 6]])

# print(N)
# print(N.T)

# print(N + 5)
# print(N * 5)
# print(N / 5)


# print(M+N)
# print(M-N)
# print(M*N)
# print(M/N)
# print(M//N)

# print(M@N.T)
# print(N@M.T)


# c = np.array([2, 4])
# print(c@N)


X = np.arange(3*4*5)
X = X.reshape((3, 4, 5))

# print(X.shape)
# print(X)

# print("\n---\n\n")

# print(X[0, 3, 3])
# print(X[:, 1, :])
# print(X[1, :, 1])

# print("\n---\n\n")

# print(X[1, 1, 1:])
# print(X[1][1][1:])



print(
    np.array([[3, 5, 1], [2, 9, 3]]),
    np.arange(2, 16, 5),
    np.linspace(2, 16, 5),
    np.linspace([1, 3, 5], [5, 9, 13], 5),
    np.random.rand(50) * 100,
    np.random.randint(15, 25, (3, 5)),

    np.eye(4, dtype=int) * 9 ,
    np.ones((4, 5), dtype=int) * 5,
    np.zeros_like(X),

    np.tile([[2, 3], [5, 1]], (3, 2)),

    np.random.choice([1, 5, 7], (12, 12), p=[0.5, 0.4, 0.1]),
    sep="\n\n"
)