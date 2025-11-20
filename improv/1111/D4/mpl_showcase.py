from matplotlib import pyplot as plt
import numpy as np
from matplotlib.axes import Axes

# x = np.linspace(0, 2*np.pi, 100)
# y = np.sin(x)

# plt.plot(x, y)
# plt.show()

# fig, axes = plt.subplots(2, 2)
# # axes = np.array(axes).reshape(-1)
# axes = np.reshape(axes, -1)

# for i, n in enumerate([5, 10, 50, 100]):
#     x = np.linspace(0, 2*np.pi, n)
#     y = np.sin(x)

#     p:Axes = axes[i]
#     p.plot(x, y, label=f"sin(x) for {n} points")
#     p.grid()
#     p.set_xlabel(f"{n} points of x")
#     p.set_ylabel(f"sin(x)")

# plt.show()

kategorie = list("ABCD")
hodnoty = np.random.randint(10, 50, (4, 4))
barvy = ["skyblue", "orange", "green", "red"]

# for i, n in enumerate(hodnoty):
#     p:Axes = axes[i]
#     p.bar(kategorie, hodnoty[i], color=barvy[i])
#     p.grid()

# plt.show()


# x = np.random.rand(150)
# y = np.random.rand(150)
# colors = np.random.rand(150)
# sizes = np.random.rand(150) * 1000

# plt.scatter(x, y, c=colors, s=sizes, alpha=.5, cmap="plasma")
# plt.title("Random scatter plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.colorbar()
# plt.show()


labels = ["Python", "JavaScript", "C++", "Rust"]
sizes = [45, 20, 5, 30]
explode = (0, 0, .3, 0)

plt.pie(sizes, labels=labels, autopct="%1.3f%%", startangle=90, explode=explode)
plt.title("Pie chart of programming language popularity")
plt.show()