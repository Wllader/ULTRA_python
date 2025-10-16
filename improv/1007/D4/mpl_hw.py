from matplotlib import pyplot as plt
import numpy as np
from typing import Callable

#todo A) Subplots, kde každý graf je jiného typu
#todo B) Vypočítat a Vykreslit (pomocí pyplotu) aproximaci integrálu funkce (ideálně obecné, pokud nepůjde tak f=np.abs(np.sin(x)) )


def integral(x0, x1, steps:int=100, f:Callable=lambda x_: np.abs(np.sin(x_))) -> float:
    x = np.linspace(x0, x1, steps, endpoint=False)
    dx:float = abs(x[1] - x[0])
    y = f(x)

    return (y * dx).sum()

def draw_integral(x0, x1, steps_f:int=100, steps_i:int=20, f:Callable=lambda x_: np.abs(np.sin(x_))):
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
        ...

    def set_function(self, ...):
        ...

    def draw(self, ...):
        ...

    def calculate(self, ...):
        ...

    def draw_calculate(self, ...):
        ...


if __name__ == "__main__":
    I = Integrator(np.sin)

    I.draw_calculate(...)

    I.set_function(lambda x: np.abs(np.cos(x))**2)
    I.draw_calculate(...)
