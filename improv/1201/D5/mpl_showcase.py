from matplotlib import pyplot as plt
import numpy as np
from matplotlib.axes import Axes

x = np.linspace(0, 2*np.pi, 100)
# y = np.sin(x)

# plt.plot(x, y)
# plt.show()

fig, axes = plt.subplots(2, 2)
axes = np.reshape(axes, -1)

# for i, n in enumerate([5, 10, 50, 100]):
#     x = np.linspace(0, 2*np.pi, n)
#     y = np.cos(x)

#     p:Axes = axes[i]
#     p.plot(x, y, label=f"cos(x) for {n} points")
#     p.grid(True)
#     p.set_xlabel(f"{n} points of x")
#     p.set_ylabel("sin(x)")


# kategorie = list("ABCD")
# hodnoty = np.random.randint(10, 50, (4, 4))
barvy = ["skyblue", "orange", "green", "red"]

# for i, arr in enumerate(hodnoty):
#     p:Axes = axes[i]
#     p.bar(kategorie, arr, color=barvy[i])
#     p.grid(True)


# x = np.random.rand(150)
# y = np.random.rand(150)
# colors = np.random.rand(150)
sizes = np.random.rand(150) * 1000

# plt.scatter(x, y, c=colors, s=sizes, alpha=.5, cmap="Spectral")
# plt.title("Random scatter plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.colorbar()
# plt.grid()


labels = ["Python", "JavaScript", "C++", "Rust"]
sizes = [45, 20, 5, 100]
explode = (0, 0, .3, 0)

# plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, explode=explode)
# plt.title("Pie chart of programming languages popularity")



p:Axes = axes[0]
x = np.linspace(-3*np.pi, 3*np.pi, 100)
p.plot(x, np.cos(x))

p:Axes = axes[1]
p.bar(labels, sizes, color=barvy)

p:Axes = axes[2]
x = np.random.rand(150)
y = np.random.rand(150)
p.scatter(x, y, c=np.random.rand(len(x)), s=np.random.rand(len(x))*1000, alpha=.5)

p:Axes = axes[3]
p.pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%", startangle=120, colors=barvy)


plt.show()


