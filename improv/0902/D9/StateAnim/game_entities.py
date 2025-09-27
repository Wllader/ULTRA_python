import pygame as pg, numpy as np
from game_controller import GameController
from spritesheet_mr_d import SpriteSheet
from enum import Enum, auto

class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, size:tuple[int], init_pos:tuple[int]):
        super().__init__()

        self.screen = screen
        self._image = pg.Surface(size, pg.SRCALPHA)
        self.rect = self._image.get_rect(topleft=init_pos)

        self.gravity = 6

        self.gc = GameController()

    @property
    def image(self):
        self._image.fill((260, 100, 20))
        return self._image
    
    @property
    def dt(self):
        return self.gc.dt
    
    def window_correction(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > (h := self.screen.get_height()):
            self.rect.bottom = h

        w = self.screen.get_width()
        if self.rect.right < 0:
            self.rect.left = w
        elif self.rect.left > w:
            self.rect.right = 0


class Dino(Entity):
    def __init__(self, screen, size, init_pos, spritesheet:SpriteSheet=None, speed:float= 5.):
        super().__init__(screen, size, init_pos)

    def update(self):
        ...


        self.window_correction()