import numpy as np
from matplotlib import pyplot as plt


# x = lambda x: np.linspace(-np.pi/4, 2*np.pi, x)


# fig, axes = plt.subplots(2, 2)
# axes = np.array(axes).reshape(-1)

# for i, x_ in enumerate([5, 10, 50, 100]):
#     y = np.sin(x(x_))

#     axes[i].plot(x(x_), y, label="sin(x)")
#     axes[i].grid(True)
#     axes[i].set_xlabel("x")
#     axes[i].set_ylabel("sin(x)")

# plt.tight_layout()
# plt.show()


# kategorie = list("ABCD")
# hodnoty = np.random.randint(10, 50, (4, 4))
barvy = ["skyblue", "orange", "green", "red"]
# print(hodnoty)

# fig, axes = plt.subplots(2, 2)
# axes = np.array(axes).reshape(-1)

# for i, x_ in enumerate(hodnoty):
#     axes[i].grid()
#     axes[i].bar(kategorie, hodnoty[i], color=barvy[i])

# plt.show()


# x = np.random.rand(150)
# y = np.random.rand(150)

# colors = np.random.rand(150)
# sizes = np.random.rand(150) * 1000

# plt.scatter(x, y, c=colors, s=sizes, alpha=.4)
# plt.title("Random scatter plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.colorbar()
# plt.show()



labels = ["Python", "Java", "C++", "Ruby"]
# sizes = [45, 30, 15, 10]
# explode = (0, 0, 0.1, 0)

# plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, explode=explode)
# plt.title("Pie chart of programming language popularity")
# plt.show()



fig, axes = plt.subplots(2, 2)
axes = np.array(axes).reshape(-1)

x = np.linspace(-np.pi/2, 2*np.pi, 100)
axes[0].plot(x, np.cos(x))
axes[0].plot(x, np.sin(x), color="orange")


sizes = np.random.rand(4)
sizes = sizes/sizes.sum() * 100
axes[1].bar(labels, sizes, color=barvy)

x = np.random.rand(50)
y = np.random.rand(len(x))
axes[2].scatter(x, y, c=np.random.rand(len(x)), s=np.random.rand(len(x))*1000, alpha=0.4)

axes[3].pie(sizes, explode=(0, 0, .1, .2), autopct="%1.1f%%", startangle=120, colors=barvy)

plt.tight_layout()
plt.show()