from typing import Callable
from numpy import clip, ndarray, pi, pow, sin
from pygame.time import Clock

class Tween:
    def __init__(self, total_time_ms:int = 1000, tween:Callable = lambda t: t, clipped:bool = False):
        self.total_time = total_time_ms
        self.current_time = 0

        self.clk = Clock()
        self.tween = tween

        self.clipped = clipped

    def get_state(self, A, B):
        self.current_time += self.clk.tick()
        t0 = self.current_time / self.total_time
        t = clip(t0, 0, 1) if self.clipped else t0

        x0 = self.tween(t)
        x = clip(x0, 0, 1) if self.clipped else x0
        output = (1-x)*A + x*B

        return output, t >= 1
    
    def tweenify(self, start:ndarray, stop:ndarray):
        if(start != stop).any():
            state, finished = self.get_state(start, stop)
            if finished:
                start[:] = stop
                return stop
            return state
        return start

    def reset(self):
        self.current_time = 0
        self.clk.tick()

    @staticmethod
    def EaseInOutCubic(total_time_ms:int = 1000, clipped:bool = False) -> "Tween":
        return Tween(
            total_time_ms,
            lambda t: 4*t**3 if t < 0.5 else 1 - (-2*t + 2)**3 / 2,
            clipped
        )
    
    @staticmethod
    def EaseOutBounce(total_time_ms:int=1000, clipped:bool = False) -> "Tween":
        def ease_out_bounce(t):
            n = 7.5625
            d = 2.75

            if t < 1/d:
                return n * t**2
            elif t < 2/d:
                t -= 1.5 / d
                return n * t**2 + .75
            elif t < 2.5/d:
                t -= 2.25/d
                return n * t**2 + .9375
            else:
                t -= 2.625/d
                return n * t**2 + 0.984375
            
        return Tween(
            total_time_ms,
            ease_out_bounce,
            clipped
        )
    

    @staticmethod
    def EaseInOutBounce(total_time_ms:int=1000, clipped:bool = False) -> "Tween":
        ease_out_bounce = Tween.EaseOutBounce(total_time_ms).tween

        def ease_in_out_bounce(t):
            if t < 0.5:
                return (1 - ease_out_bounce(1 - 2*t)) / 2
            else:
                return (1 + ease_out_bounce(2*t - 1)) / 2
            
        return Tween(
            total_time_ms,
            ease_in_out_bounce,
            clipped
        )
    

    @staticmethod
    def EaseInElastic(total_time_ms:int=1000, clipped:bool = False) -> "Tween":
        c = (2*pi)/3

        def foo(t):
            if t == 0:
                return 0
            elif t == 1:
                return 1
            else:
                return -pow(2, 10*(t-1)) * sin(c * (t * 10 - 10.75))
            
        return Tween(
            total_time_ms,
            foo,
            clipped
        )