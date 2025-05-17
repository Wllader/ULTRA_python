from numpy import array
from pygame.time import Clock
import pygame as pg

class GameController(object):
    def __init__(self):
        self.scores = array([0, 0])
        self.clock = Clock()
        self.dt = 0

    def __new__(self):
        if not hasattr(self, "instance"):
            self.instance = super(GameController, self).__new__(self)
        return self.instance
    
    def score(self, player:int):
        self.scores[player] += 1

    def get_score(self, player:int|None = None):
        if player is None:
            return self.scores
        return self.scores[player]
    
    def tick(self, fps:int, factor = 10):
        self.dt = self.clock.tick(fps) / factor