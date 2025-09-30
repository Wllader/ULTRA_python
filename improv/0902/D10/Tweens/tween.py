from typing import Callable
from numpy import clip, ndarray, pow
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
    def EaseOutQuint(total_time_ms:int=1000, clipped:bool = False) -> "Tween":
        return Tween(
            total_time_ms,
            lambda t: 1 - pow(1-t, 5),
            clipped
        )