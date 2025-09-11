from matplotlib import pyplot as plt
import numpy as np

# x = np.linspace(-5*np.pi, 3*np.pi, 100)
# y = np.sin(x)

# plt.plot(x, y)
# plt.show()

# fig, axes = plt.subplots(2, 2)
# axes = np.array(axes).reshape(-1)

# for i, n in enumerate([5, 10, 50, 100]):
#     x = np.linspace(-np.pi/4, 2*np.pi, n)
#     y = np.sin(x)

#     p = axes[i]

#     p.plot(x, y, label=f"sin(x) for {n} points")
#     p.grid()
#     p.set_xlabel(f"{n} points of x")
#     p.set_ylabel("sin(x)")

# plt.show()


# kategorie   = list("ABCD")
# hodnoty     = np.random.randint(10, 50, (4, 4))
# barvy       = ["skyblue", "orange", "green", "red"]

# for i, n in enumerate(hodnoty):
#     p = axes[i]

#     p.grid()
#     p.bar(kategorie, hodnoty[i], color=barvy[i])

# plt.show()


# x = np.random.rand(150)
# y = np.random.rand(150)
# colors = np.random.rand(150)
# sizes = np.random.rand(150) * 1000

# plt.scatter(x, y, c=colors, s=sizes, alpha=.5)
# plt.title("Random scatter plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.colorbar()

# plt.show()


# labels = ["Python", "Java", "C++", "Rust"]
# sizes = [45, 30, 15, 10]
# explode = (0, 0, 0, 0.1)

# plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=45, explode=explode)
# plt.title("Pie chart of programming language popularity")

# plt.show()