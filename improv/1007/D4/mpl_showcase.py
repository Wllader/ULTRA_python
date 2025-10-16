from matplotlib import pyplot as plt
import numpy as np

# x = np.linspace(-2*np.pi, 3*np.pi, 1000)
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


# kategorie = list("ABCD")
# hodnoty = np.random.randint(10, 50, (4, 4))
barvy = ["skyblue", "orange", "green", "red"]

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


labels = ["Python", "Java", "C++", "Rust"]
# sizes = [45, 20, 5, 30]
explode = (0, 0, 0.3, 0)

# plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, explode=explode)
# plt.title("Pie chart of programming language popularity")

# plt.show()


fig, axes = plt.subplots(2, 2)
axes = np.array(axes).reshape(-1)

x = np.linspace(-np.pi/2, 2*np.pi, 50)
axes[0].plot(x, np.cos(x))

sizes = np.random.rand(4)
sizes = sizes/sizes.sum()
axes[1].bar(labels, sizes, color=barvy)

x = np.random.rand(50)
y = np.random.rand(len(x))
axes[2].scatter(x, y, c=np.random.rand(len(x)), s=np.random.rand(len(x))*1000, alpha=.5)

axes[3].pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%", startangle=120, colors=barvy)


plt.tight_layout()
plt.show()
