import numpy as np
from matplotlib import pyplot as plt


# def integral(x1, x2, f = np.sin, steps = 100):
#     x = np.linspace(x1, x2, steps)
#     dx = abs(x[1] - x[0])

#     return (f(x[:-1]) * dx).sum()

# def draw_integral(x1, x2, f=np.sin, steps=20):
#     x = np.linspace(x1, x2, steps)
#     dx = abs(x[1] - x[0])

#     plt.plot(x, f(x))
#     plt.fill_between(x, f(x), 0, color="orange", alpha=0.5)
#     for i in range(len(x) - 1):
#         plt.fill_between([x[i], x[i] + dx], [f(x[i]), f(x[i])], 0, color="red", alpha=0.5)

#     plt.show()


class Integrator:
    def __init__(self, f):
        self.set_function(f)

    def set_function(self, f):
        self.f = f

    def draw(self, x1, x2, steps=30):
        x = np.linspace(x1, x2, steps)
        dx = abs(x[1] - x[0])

        plt.plot(x, self.f(x))
        plt.fill_between(x, self.f(x), 0, color="orange", alpha=0.5)
        for i in range(len(x) - 1):
            plt.fill_between([x[i], x[i] + dx], [self.f(x[i]), self.f(x[i])], 0, color="red", alpha=0.5)

        plt.show()

    def calculate(self, x1, x2, steps=100):
        x = np.linspace(x1, x2, steps)
        dx = abs(x[1] - x[0])

        return (self.f(x[:-1]) * dx).sum()

    def draw_calculate(self, x1, x2, steps_c=100, steps_d=30):
        print(self.calculate(x1, x2, steps_c))
        self.draw(x1, x2, steps_d)

I = Integrator(lambda x: np.abs(np.sin(x)))

# print(I.calculate(np.pi, 3*np.pi))
# I.draw(np.pi, 3*np.pi)
I.draw_calculate(np.pi, 3*np.pi, steps_c=1000)
I.set_function(lambda x: np.cos(x) - 1)
I.draw_calculate(np.pi, 3*np.pi, steps_c=1000, steps_d=150)

