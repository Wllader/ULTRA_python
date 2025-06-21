from typing import Callable
from numpy import clip
from pygame.time import Clock


class Tween:
    def __init__(self, total_time_ms:int = 1000, tween:Callable = lambda t: t):
        self.total_time = total_time_ms
        self.current_time = 0

        self.clk = Clock()
        self.tween = tween

    def get_state(self, A, B):
        self.current_time += self.clk.tick()
        t = clip(self.current_time / self.total_time, 0, 1)

        x = clip(self.tween(t), 0, 1) #!
        output = (1-x)*A + x*B

        return output, x >= 1
    
    def reset(self):
        self.current_time = 0
        self.clk.tick()


    @staticmethod
    def EaseInOutCubic(total_time_ms):
        return Tween(
            total_time_ms,
            lambda t: 4*t**3 if t < 0.5 else 1 - (-2*t + 2)**3 / 2
        )
    
    @staticmethod
    def EaseOutBounce(total_time_ms):
        def ease_out_bounce(t):
            n = 7.5625
            d = 2.75

            if t < 1 / d:
                return n * t**2
            elif t < 2 / d:
                t -= 1.5 / d
                return n * t**2 + 0.75
            elif t < 2.5 / d:
                t -= 2.25 / d
                return n * t**2 + 0.9375
            else:
                t -= 2.625 / d
                return n * t**2 + 0.984375

        return Tween(
            total_time_ms,
            ease_out_bounce
        )


    @staticmethod
    def EaseInOutBounce(total_time_ms):
        def ease_in_out_bounce(t):
            if t < 0.5:
                return (1 - ease_out_bounce(1 - 2*t)) / 2
            else:
                return (1 + ease_out_bounce(2*t - 1)) / 2
            
        ease_out_bounce = Tween.EaseOutBounce(total_time_ms).tween


        return Tween(
            total_time_ms,
            ease_in_out_bounce
        )
