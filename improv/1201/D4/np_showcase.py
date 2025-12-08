import numpy as np

a = np.array([1, 2, 3])
b = np.array([5, 6, 7])

print(
    a, b,
    3*a,
    b*5,
    a / 3,
    b // 5,
    a + 12,

    a + b, 
    a * b,
    a / b,
    b // a,
    b % a,

    np.dot(a, b),
    a.dot(b),
    a @ b,

    sep="\n--\n",
    end="\n\n==\n\n"
)


A = np.array([[4, 5, 6], [1, 2, 3]])
B = np.array([
    [4, 5],
    [6, 7],
    [8, 9]
])

print(
    A, B,
    A*5, B-2,

    B.T,
    A + B.T,

    A < B.T,
    (A < B.T).all(),
    np.where(A >= 3, -5, B.T),

    A @ B,
    B @ A,

    sep="\n---\n",
    end="\n\n==\n\n"
)



a = np.arange(3*4*5)
a = a.reshape((3, 4, 5))
print(
    a.shape, a,
    a[0],
    a[0, 1],
    a[0, 1, 2],

    a[:, 1, :],
    a[:, 1, 1],
    a[1, :, 1],

    a[1][:][1], #! 

    sep="\n---\n",
    end="\n\n==\n\n"
)


a = np.array([[3, 5, 1], [2, 9, 3]])
print(
    np.arange(2, 26),
    np.arange(2, 26, 5, dtype=float),
    np.linspace(2, 16, 5, dtype=int, endpoint=False),

    np.eye(4, 5, dtype=int) * 5,
    np.ones((4, 6)) / 4,
    np.zeros((6, 4), dtype=bool),
    np.ones_like(a),

    np.tile(a, (4, 3)),

    np.random.randint(2, 16, (3, 2)),
    np.random.rand(5, 3) * 20 + 20,
    np.random.choice([1, 5, 7], (8, 8), p=[.5, .4, .1]) == 7,


    sep="\n---\n",
    end="\n\n==\n\n"
)