import numpy as np


# l = [1, True, "string"]
# a = np.array([1, 2, 3])
# b = np.array([5, 6, 7])


# print(
#     a, b,
#     3 * a,
#     a // 2,
#     a + b,
#     a * b,
#     a / b,
#     np.dot(a, b),
#     a @ b,

#     sep="\n---\n"
# )


# A = np.array([[1,2,3], [4,5,6]])
# B = np.array([[4,5], [6,7], [8,9]])

# print(
#     f"{A=}\n{B=}",
#     f"{A.T=}\n{B.T=}",
#     f"{A + B.T=}",
#     f"{A / B.T=}",
#     f"{A > B.T=}",
#     f"{A @ B=}",
#     f"{B @ A=}",

#     sep="\n---\n"
# )


# a = np.arange(3*4*5)
# a = a.reshape((3, 4, 5))

# print(
#     a.shape,
#     a,
#     a[1],
#     a[1, 1],
#     a[1, 1, 1],

#     a[:, 1, :],
#     a[:, 1, 1],
#     a[1, :, 1], #! -------------<
#                 #!              |
#     a[1][:][1], #! Není stejné -^

#     sep="\n---\n"
# )


a = np.array([[3,5,1],[2,9,3]])
print(
    np.arange(2, 16),
    np.linspace(2, 16, 5, dtype=int),
    np.linspace([1, 3, 5], [5, 9, 13], 5),
    np.random.randint(2, 16, (3, 2)),
    np.eye(4, 12, dtype=int) * 5,
    np.ones((4, 6), dtype=int) * 17,
    np.tile(a, (3, 2)),

    np.ones_like(a) / 8,

    np.random.choice([1, 5, 7], (8, 8), p=[0.5, .4, .1]) == 7,

    sep="\n---\n"
)