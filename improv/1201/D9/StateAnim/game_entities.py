import pygame as pg, numpy as np
from game_controller import GameController
from spritesheet_mr_d import SpriteSheet
from enum import Enum, auto

class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, size:tuple[int], init_pos:tuple[int], spritesheet:SpriteSheet=None):
        super().__init__()


    @property
    def image(self): pass

    @property
    def rect(self): pass

    @property
    def dt(self): pass

    def window_correction(self): pass
        #Pacman-style

class Dino(Entity):
    def __init__(self, screen, size, init_pos, spritesheet = None, speed:float=6.):
        super().__init__(screen, size, init_pos, spritesheet)


    def update(self):
        # Left/Right movement
        pass