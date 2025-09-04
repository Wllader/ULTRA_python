from numpy import array
from pygame.time import Clock

class GameController:
    def __init__(self):
        self.clock = Clock()
        self.dt = 0

    def __new__(self):
        if not hasattr(self, "instance"):
            self.instance = super(GameController, self).__new__(self)
        return self.instance
    
    def tick(self, fps:int, factor:10):
        self.dt = self.clock.tick(fps) / factor