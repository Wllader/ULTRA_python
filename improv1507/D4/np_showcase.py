import numpy as np


# l = [1, True, "string", [1, 2, "ahoj"], (1, "a")]
# a = np.array([1, 2, 3])
# b = np.array([5, 6, 7])


# print(
#     a, b,
#     3 * a,
#     a // 3,
#     a + b,
#     a * b,
#     a / b,
#     np.dot(a, b),
#     a @ b

#     ,sep="\n---\n"
# )

# A = np.array([[1, 2, 3], [4, 5, 6]])
# B = np.array([[4, 5], [6, 7], [8, 9]])

# print(
#     A, B,
#     A.T, B.T,
#     A + B.T,
#     A / B.T,
#     A > B.T,
#     A @ B,
#     B @ A

#     ,sep="\n---\n"
# )





# a = np.arange(3*4*5)
# a = a.reshape((3, 4, 5))
# print(
#     a.shape,
#     a,
#     # a[1],
#     # a[1, 1],
#     # a[1, 1, 1],

#     # a[:, 1, :],
#     # a[:, 1, 1],
#     # a[1, :, 1],
    
#     a[1][1::2][:]

#     ,sep="\n---\n"
# )


a = np.array([[3, 5, 1],[2, 9, 3]])
print(
    np.arange(2, 16),
    np.linspace(2, 16, 5, dtype=int),
    np.linspace([1, 3, 5], [5, 9, 13], 5),
    np.random.randint(2, 16, (3, 5)),
    np.eye(4, 12, dtype=int) * 5,
    np.ones((13, 8), dtype=int),
    np.tile(a, (3, 2)),

    np.ones_like(a, dtype=float) / 8,

    np.random.choice([1, 5, 7], (12, 12), p=[0.5, .4, .1]) == 7


    ,sep="\n---\n"
)