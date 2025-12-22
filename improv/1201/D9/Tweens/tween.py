from typing import Callable
from numpy import clip, ndarray, sin, pi, pow
from pygame.time import Clock

class Tween:
    def __init__(self, total_time_ms:int=1000, tween:Callable=lambda t:t):
        self.total_time = total_time_ms
        self.current_time = 0

        self.clk = Clock()
        self.tween = tween

    def get_state(self, A, B):
        self.current_time += self.clk.tick()
        t = self.current_time / self.total_time
        t = clip(t, 0, 1)

        x = self.tween(t)

        output = (1-x)*A + x*B
        return output, t >= 1
    
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
    def EaseOutSine(total_time_ms:int=1000) -> "Tween":
        return Tween(total_time_ms, lambda t: sin((t * pi) / 2))
    

    @staticmethod
    def EaseInOutExpo(total_time_ms:int=1000) -> "Tween":
        def easeInOutExpo(t:float) -> float:
            if t == 0: return 0
            if t == 1: return 1

            if t < 0.5:
                return pow(2, 20*t-10) / 2
            else:
                return (2 -pow(2, -20*t+10)) / 2
            
        return Tween(total_time_ms, easeInOutExpo)
    
    @staticmethod
    def EaseOutBounce(total_time_ms:int=1000) -> "Tween":
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
            ease_out_bounce
        )
    

    @staticmethod
    def EaseInOutBounce(total_time_ms:int=1000) -> "Tween":
        ease_out_bounce = Tween.EaseOutBounce(total_time_ms).tween

        def ease_in_out_bounce(t):
            if t < 0.5:
                return (1 - ease_out_bounce(1-2*t)) / 2
            else:
                return (1 + ease_out_bounce(2*t-1)) / 2
            
        return Tween(
            total_time_ms,
            ease_in_out_bounce
        )