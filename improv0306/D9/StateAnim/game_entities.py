import pygame as pg, numpy as np
from game_controller import GameController

class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, size:np.ndarray, init_pos:np.ndarray):
        super().__init__()

        self.screen = screen
        self._image = pg.Surface(size)
        self._rect = self._image.get_rect(topleft=init_pos)
        self.gravity = 10

        self.gc = GameController()

    @property
    def image(self):
        self._image.fill((160, 100, 20))
        return self._image
    
    @property
    def rect(self):
        return self._rect
    
    @property
    def dt(self):
        return self.gc.dt
    
    def window_correction(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > (h := self.screen.get_height()):
            self.rect.bottom = h

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > (w := self.screen.get_width()):
            self.rect.right = w    


class Dino(Entity):
    def __init__(self, screen, size, init_pos, speed:float=5., jmp_pwr:float=150):
        super().__init__(screen, size, init_pos)

        self.speed = speed
        self.jmp_pwr = jmp_pwr

    
    @property
    def grounded(self):
        return self._rect.bottom == self.screen.get_height()

    
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self._rect.x -= self.speed * self.dt
        if keys[pg.K_d]:
            self._rect.x += self.speed * self.dt

        if keys[pg.K_w] and self.grounded:
            self._rect.y -= self.jmp_pwr * self.dt

        # Gravity
        self._rect.y += self.gravity * self.dt


        self.window_correction()