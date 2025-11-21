from matplotlib import pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from typing import Callable

# labels = ["Python", "JavaScript", "C++", "Rust"]
# barvy = ["skyblue", "orange", "green", "red"]
# sizes = [45, 20, 5, 30]
# explode = (0, 0, .3, 0)


# fig, axes = plt.subplots(2, 2)
# axes:list[Axes] = np.reshape(axes, -1)

# x = np.linspace(-np.pi/2, 2*np.pi, 50)
# axes[0].plot(x, np.cos(x))

# sizes = np.random.rand(4)
# sizes = sizes/sizes.sum()
# axes[1].bar(labels, sizes, color=barvy)


# x = np.random.rand(50)
# y = np.random.rand(len(x))
# axes[2].scatter(x, y, c=np.random.rand(len(x)), s=np.random.rand(len(x))*1000, alpha=.5)

# axes[3].pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%", startangle=120, colors=barvy)

# plt.tight_layout()
# plt.show()


def integral(x0, x1, steps:int=100, f:Callable=lambda x_: np.abs(np.cos(x_))) -> float:
    x = np.linspace(x0, x1, steps, endpoint=False)
    dx:float = abs(x[1] - x[0])
    y = f(x)

    return (y * dx).sum()

def draw_integral(x0, x1, steps_f:int=100, steps_i:int=20, f:Callable=lambda x_: np.abs(np.cos(x_))):
    x_f = np.linspace(x0, x1, steps_f)
    x_i = np.linspace(x0, x1, steps_i, endpoint=False)
    
    y_i = f(x_i)
    dx = abs(x_i[1] - x_i[0])

    plt.plot(x_f, f(x_f))
    plt.fill_between(x_f, f(x_f), color="skyblue", alpha=.5)
    for i in range(len(x_i)):
        plt.fill_between(
            [x_i[i], x_i[i] + dx], [y_i[i], y_i[i]], color="red", alpha=.5
        )

    plt.show()


class Integrator:
    def __init__(self, f:Callable):
        self.set_function(f)

    def set_function(self, f:Callable):
        self.f = f

    def draw(self, x0, x1, steps_f:int=100, steps_i:int=20):
        x_f = np.linspace(x0, x1, steps_f)
        x_i = np.linspace(x0, x1, steps_i, endpoint=False)
        
        y_i = self.f(x_i)
        dx = abs(x_i[1] - x_i[0])

        plt.plot(x_f, self.f(x_f))
        plt.fill_between(x_f, self.f(x_f), color="skyblue", alpha=.5)
        for i in range(len(x_i)):
            plt.fill_between(
                [x_i[i], x_i[i] + dx], [y_i[i], y_i[i]], color="red", alpha=.5
            )

        plt.show()

    def calculate(self, x0, x1, steps:int=100):
        x = np.linspace(x0, x1, steps, endpoint=False)
        dx:float = abs(x[1] - x[0])
        y = self.f(x)

        return (y * dx).sum()

    def draw_calculate(self, x0, x1, steps_c=100, steps_d=30):
        print(self.calculate(x0, x1, steps_c))
        self.draw(x0, x1, steps_c, steps_d)


if __name__ == "__main__":
    I = Integrator(np.sin)
    I.draw_calculate(0, 2*np.pi)

    I.set_function(lambda x: np.abs(np.cos(x)**2 - .5))
    I.draw_calculate(-np.pi, 0)