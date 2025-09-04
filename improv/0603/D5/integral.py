import numpy as np
from matplotlib import pyplot as plt
from typing import Callable

def integral(x1, x2, steps:int = 100, f:Callable = lambda x: np.abs(np.sin(x))) -> float:
    x = np.linspace(x1, x2, steps, endpoint=False)
    dx = abs(x[1] - x[0])

    return (f(x) * dx).sum()


def draw_integral(x1, x2, steps_f:int=100, steps_i=20, f:Callable = lambda x: np.abs(np.sin(x))) -> None:
    x_f = np.linspace(x1, x2, steps_f)
    x_i = np.linspace(x1, x2, steps_i)
    dx = np.abs(x_i[1] - x_i[0])

    plt.plot(x_f, f(x_f))
    for i in range(len(x_i) - 1):
        plt.fill_between((x_i[i], x_i[i] + dx), (f(x_i[i]), f(x_i[i])), color="red", alpha=.5)

    plt.show()


class Integrator:
    def __init__(self, f:Callable):
        self.set_function(f)

    def set_function(self, f:Callable):
        self.f = f

    def draw(self, x1, x2, steps_i=30, steps_f=100):
        x_f = np.linspace(x1, x2, steps_f)
        x_i = np.linspace(x1, x2, steps_i)
        dx = np.abs(x_i[1] - x_i[0])

        plt.plot(x_f, self.f(x_f))
        plt.fill_between(x_f, self.f(x_f), color="skyblue", alpha=0.5)
        for i in range(len(x_i) - 1):
            plt.fill_between((x_i[i], x_i[i] + dx), (self.f(x_i[i]), self.f(x_i[i])), color="red", alpha=.5)

        plt.show()

    def calculate(self, x1, x2, steps=100):
        x = np.linspace(x1, x2, steps, endpoint=False)
        dx = abs(x[1] - x[0])

        return (self.f(x) * dx).sum()
    
    def draw_calculate(self, x1, x2, steps_c=100, steps_d=30):
        print(self.calculate(x1, x2, steps_c))
        self.draw(x1, x2, steps_d, steps_c)


if __name__ == "__main__":
    I = Integrator(np.sin)

    I.draw_calculate(-5, 12, steps_c=500)
    I.set_function(lambda x: np.abs(np.cos(x))**2)

    I.draw_calculate(-12, 5, steps_c=500)