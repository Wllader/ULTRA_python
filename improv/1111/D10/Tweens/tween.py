from typing import Callable
from numpy import clip, ndarray
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
        x = self.tween(t)

        output = (1-x)*A + x*B
        return output, t >= 1
    
    def reset(self):
        self.current_time = 0
        self.clk.tick()