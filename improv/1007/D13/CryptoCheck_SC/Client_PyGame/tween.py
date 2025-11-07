from typing import Callable
from numpy import clip, ndarray, sin, pi
from pygame.time import Clock

class Tween:
    def __init__(self, total_time_ms:int=1000, tween:Callable=lambda t:t, clipped:tuple=None):
        self.total_time = total_time_ms
        self.current_time = 0

        self.clk = Clock()
        self.tween = tween

        self.clipped = clipped

    def get_state(self, A, B):
        self.current_time += self.clk.tick()
        t = self.current_time / self.total_time
        x = self.tween(t)

        output = (1-x)*A + x*B
        
        return clip(output, *self.clipped) if self.clipped is not None else output, t >= 1
    
    def reset(self):
        self.current_time = 0
        self.clk.tick()

    def tweenify(self, start:ndarray, stop:ndarray):
        if (start != stop).any():
            state, finished = self.get_state(start, stop)
            if finished:
                start[:] = stop
                return stop
            return state
        return start
    

    @staticmethod
    def EaseOutSine(total_time_ms:int=1000, clipped:tuple=None) -> "Tween":
        return Tween(
            total_time_ms,
            lambda t: sin(t*pi / 2),
            clipped
        )
    
    @staticmethod
    def EaseOutBounce(total_time_ms:int=1000, clipped:tuple=None) -> "Tween":
        def ease_out_bounce(t):
            n = 7.5625
            d = 2.75

            if t < 1/d:
                return n*t*t
            elif t < 2/d:
                t -= 1.5/d
                return n*t*t + 0.75
            elif t < 2.5/d:
                t -= 2.25/d
                return n*t*t + 0.9375
            else:
                t -= 2.625/d
                return n*t*t + 0.984375
            
        return Tween(
            total_time_ms,
            ease_out_bounce,
            clipped
        )
    
    @staticmethod
    def EaseInOutBounce(total_time_ms:int=1000, clipped:tuple=None) -> "Tween":
        ease_out_bounce = Tween.EaseOutBounce(total_time_ms).tween

        def ease_in_out_bounce(t):
            if t < 0.5:
                return (1 - ease_out_bounce(1-2*t)) / 2
            else:
                return (1 + ease_out_bounce(2*t-1)) / 2
            
        return Tween(
            total_time_ms,
            ease_in_out_bounce,
            clipped
        )