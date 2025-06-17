import pygame as pg, numpy as np
from abc import ABC


class PongEntity(pg.sprite.Sprite, ABC):
    def __init__(
            self,
            screen:pg.Surface,
            size:np.ndarray,
            init_center_pos:np.ndarray,
            speed:np.ndarray,
            color:np.ndarray
        ):
        super().__init__()

        self.screen = screen
        self.image = pg.Surface(size)
        self.rect = self.image.get_rect(center=init_center_pos)
        self.color = color
        self.image.fill(color)
        self.speed = speed


    def update(self):
        self.window_correction()

    def window_correction(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > (h := self.screen.get_height()):
            self.rect.bottom = h

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > (w := self.screen.get_width()):
            self.rect.right = w


class PongPlayer(PongEntity):
    def update(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed[1] * dt

        if keys[pg.K_s]:
            self.rect.y += self.speed[1] * dt

        self.window_correction()

class PongBot(PongEntity):
    pass

class PongBall(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color):
        super().__init__(screen, size, init_center_pos, speed, color)

        self.g_bounce = pg.sprite.Group()

    def update(self, dt):
        self.rect.x += self.speed[0] * dt
        self.rect.y += self.speed[1] * dt

        self.window_correction()
        self.bounce()

    
    def bounce(self):
        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height():
            self.speed[1] *= -1

        if self.rect.left <= 0 or self.rect.right >= self.screen.get_width():
            self.speed[0] *= -1


        if o := self.rect.collideobjects(list(self.g_bounce)):
            o:PongEntity

            self.speed[0] *= -1
            self.color = o.color