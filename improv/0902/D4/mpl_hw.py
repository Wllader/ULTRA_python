import numpy as np
from matplotlib import pyplot as plt
from typing import Callable


def integral(x0, x1, steps:int=100, f:Callable = lambda x_: np.abs(np.sin(x_))) -> float:
    x = np.linspace(x0, x1, steps, endpoint=False)
    dx:float = abs(x[1] - x[0])
    y = f(x)

    # print(x, y)
    return (y * dx).sum()


def draw_integral(x0, x1, steps_f:int = 100, steps_i:int = 20, f:Callable = lambda x_: np.abs(np.sin(x_))):
    x_f = np.linspace(x0, x1, steps_f)
    x_i = np.linspace(x0, x1, steps_i)
    y_i = f(x_i)
    dx = abs(x_i[1] - x_i[0])

    plt.plot(x_f, f(x_f))
    for i in range(len(x_i) - 1):
        plt.fill_between([x_i[i], x_i[i] + dx], [y_i[i], y_i[i]], color="red", alpha=.5)

    plt.show()


class Integrator:
    def __init__(self, f:Callable):
        self.set_function(f)

    def set_function(self, f:Callable):
        self.f = f

    def draw(self, x0, x1, steps_i=30, steps_f=100):
        x_f = np.linspace(x0, x1, steps_f)
        x_i = np.linspace(x0, x1, steps_i)
        y_i = self.f(x_i)
        dx = abs(x_i[1] - x_i[0])

        plt.plot(x_f, self.f(x_f))
        plt.fill_between(x_f, self.f(x_f), color="skyblue", alpha=.5)
        for i in range(len(x_i) - 1):
            plt.fill_between([x_i[i], x_i[i] + dx], [y_i[i], y_i[i]], color="red", alpha=.5)

        plt.show()

    def calculate(self, x0, x1, steps=100):
        x = np.linspace(x0, x1, steps, endpoint=False)
        dx:float = abs(x[1] - x[0])
        y = self.f(x)

        # print(x, y)
        return (y * dx).sum()
    
    def draw_calculate(self, x0, x1, steps_c=100, steps_d=30):
        print(self.calculate(x0, x1, steps_c))
        self.draw(x0, x1, steps_d, steps_c)


if __name__ == "__main__":
    I = Integrator(np.sin)
    I.draw_calculate(-5, 12, steps_c=500)
    # -0.534714354813401

    I.set_function(lambda x: np.abs(np.cos(x))**2 - 0.5)
    I.draw_calculate(-12, 5, steps_c=600)
    # -0.35335486288040496

    I.set_function(lambda x: 20 - x)
    I.draw_calculate(-5, 25, steps_c=50, steps_d=4)