from typing import Callable
from numpy import clip
from pygame.time import Clock


class Tween:
    def __init__(self, total_time, tween:Callable = lambda t: t):
        self.total_time = total_time
        self.current_time = 0

        self.clk = Clock()
        self.tween = tween

    def get_state(self, A, B):
        self.current_time += self.clk.tick()
        progress = clip(self.current_time / self.total_time, 0, 1)

        t = clip(self.tween(progress), 0, 1)
        # print(f"{t=}, {A=}, {B=}")
        output = t*B + (1-t)*A
        # print(f"{progress=}\t{t=}\t{output=}")

        return output, t >= 1
    
    def reset(self):
        self.current_time = 0
        self.clk.tick()

    @staticmethod
    def EaseInOutCubic(total_time):
        return Tween(
            total_time,
            lambda t: 4*t**3 if t < 0.5 else 1 - (-2 * t + 2)**3 / 2
        )
    
    @staticmethod
    def EaseInOutBounce(total_time):
        def ease_out_bounce(t):
            n = 7.5625
            d = 2.75

            if t < 1 / d:
                return n * t**2
            elif t < 2 / d:
                t -= 1.5 / d
                return n * t**2 + 0.75
            elif t < 2.5 / d:
                t -= 2.5 / d
                return n * t**2 + 0.9375
            else:
                t -= 2.625 / d
                return n * t**2 + 0.984375
            
        def ease_in_out_bounce(t):
            if t < 0.5:
                return (1 - ease_out_bounce(1 - 2*t)) / 2
            else:
                return (1 + ease_out_bounce(2*t - 1)) / 2
            
        return Tween(
            total_time,
            ease_in_out_bounce
        )