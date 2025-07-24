from matplotlib import pyplot as plt
import numpy as np


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



# kategorie   = list("ABCD")
# hodnoty     = np.random.randint(10, 50, (4, 4))
barvy       = ["skyblue", "orange", "green", "red"]

# for i, n in enumerate(hodnoty):
#     p = axes[i]

#     p.grid()
#     p.bar(kategorie, hodnoty[i], color=barvy[i])


# x = np.random.rand(150)
# y = np.random.rand(150)
# colors = np.random.rand(150)
# sizes = np.random.rand(150) * 1000

# plt.scatter(x, y, c=colors, s=sizes, alpha=.5)
# plt.title("Random scatter plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.colorbar()


labels = ["Python", "Java", "C++", "Ruby"]
# sizes = [45, 30, 15, 10]
explode = (0, 0, 0.1, 0)

# plt.pie(sizes, labels=labels, autopct="%1.1f%%", explode=explode, startangle=140)
# plt.title("Pie chart of programming language popularity")
# plt.axis("equal")

fig, axes = plt.subplots(2,2)
axes = np.array(axes).reshape(-1)

x = np.linspace(-np.pi/2, 2*np.pi, 50)
axes[0].plot(x, np.cos(x))

sizes = np.random.rand(4)
sizes = sizes/sizes.sum()
axes[1].bar(labels, sizes, color=barvy)

x = np.random.rand(25)
y = np.random.rand(25)
axes[2].scatter(x, y, c=np.random.rand(len(x)), s=np.random.rand(len(x))*1000, alpha=.5)

axes[3].pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%", startangle=120, colors=barvy)


plt.tight_layout()
plt.show()

