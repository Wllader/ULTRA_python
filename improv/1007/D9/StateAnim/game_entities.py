import pygame as pg, numpy as np
from game_controller import GameController
from spritesheet_sr_fc import SpriteSheet


class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, size:tuple[int], init_pos:tuple[int], spritesheet:SpriteSheet=None):
        super().__init__()

        self.screen = screen
        self.sheet = spritesheet
        self._image = pg.Surface(size, pg.SRCALPHA)
        self._rect = self._image.get_rect(topleft=init_pos)

        self.gravitiy = 6
        self.gc = GameController()

    @property
    def image(self):
        if self.sheet is None:
            self._image.fill((160, 100, 20))
        else:
            self._image = self.sheet.frame
        return self._image
    
    @property
    def rect(self):
        self._rect = self._image.get_rect(topleft=self._rect.topleft)
        return self._rect
    
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
            self.rect.bottom = 0

    def update(self):
        super().update()
        self.window_correction()


class Dino(Entity):
    def __init__(self, screen, size, init_pos, spritesheet = None, speed:float=5.):
        super().__init__(screen, size, init_pos, spritesheet)

        self.speed = speed

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -= self.speed * self.dt

        if keys[pg.K_d]:
            self.rect.x += self.speed * self.dt

        self.rect.y += self.gravitiy * self.dt

        self.window_correction()
