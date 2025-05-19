from pygame.time import Clock
from numpy import min, max, clip
from typing import Callable

class Tweens:
    def __init__(self, total_time, tween:Callable = lambda t: t):
        self.total_time = total_time
        self.current_time = 0

        self.clk = Clock()
        self.tween = tween

    def get_state(self, A, B):
        self.current_time += self.clk.tick()
        percent = min((1, self.current_time / self.total_time))

        t = clip(self.tween(percent), 0, 1)
        # t = max((0, self.tween(percent)))
        output = t*B + (1 - t)*A
        print(f"{percent=}\t{t=}\t{output=}")
        return output, percent >= 1
    
    def reset(self):
        self.current_time = 0
        self.clk.tick()

    @staticmethod
    def EaseInOutCubic(total_time):
        return Tweens(
            total_time,
            lambda t: 4*t**3 if t < 0.5 else 1 - (-2 * t + 2)**3 / 2
        )
    
    @staticmethod
    def EaseInOutBounce(total_time):
        def ease_out_bounce(t):
            n1 = 7.5625
            d1 = 2.75

            if t < 1 / d1:
                return n1 * t**2
            elif t < 2 / d1:
                t_ = t - 1.5 / d1
                return n1 * t_**2 + 0.75
            elif t < 2.5 / d1:
                t_ = t - 2.5 / d1
                return n1 * t_**2 + 0.9375
            else:
                t_ = t - 2.625 / d1
                return n1 * t_**2 + 0.984375

        def ease_in_out_bounce(t):
            if t < 0.5:
                return (1 - ease_out_bounce(1 - 2*t)) / 2
            else:
                return (1 + ease_out_bounce(2*t - 1)) / 2

        return Tweens(
            total_time,
            ease_in_out_bounce
        )
    
