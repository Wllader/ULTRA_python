import pygame as pg, numpy as np
from abc import ABC


class PongEntity(pg.sprite.Sprite, ABC):
    def __init__(
            self, 
            screen:pg.Surface,
            size:np.ndarray,
            init_center_pos:np.ndarray,
            speed:np.ndarray,
            color:np.ndarray,
            *groups
        ):
        super().__init__(*groups)

        self.screen = screen
        self.draw_func = pg.draw.rect
        self.image = pg.Surface(size)
        self.rect = self.image.get_rect(center=init_center_pos)
        self.color = color
        self.speed = speed

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value:np.ndarray):
        self._color = value
        self.image.fill((0, 0, 0, 0))
        self.draw_func(self.image, value, self.image.get_rect())

    def update(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= (h := self.screen.get_height()):
            self.rect.bottom = h

        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= (w := self.screen.get_width()):
            self.rect.right = w

class PongPlayer(PongEntity):
    def update(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed[1] * dt
        if keys[pg.K_s]:
            self.rect.y += self.speed[1] * dt

        super().update()

class PongBot(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, *groups):
        self.ball:PongBall = None

        super().__init__(screen, size, init_center_pos, speed, color, *groups)
    
    def update(self, dt):
        self.rect.centery = self.ball.rect.centery

        super().update()

class PongBall(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, *groups):
        self.bounce_group:pg.sprite.Group = None

        super().__init__(screen, size, init_center_pos, speed, color, *groups)
        self.draw_func = pg.draw.ellipse
        self.color = color

    def update(self, dt):
        self.rect.x += self.speed[0] * dt
        self.rect.y += self.speed[1] * dt

        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height():
            self.speed[1] *= -1

        if self.rect.left <= 0 or self.rect.right >= self.screen.get_width():
            self.speed[0] *= -1
            self.rect.centerx = self.screen.get_width() / 2
            self.rect.centery = self.screen.get_height() / 2
            #todo Score

        if self.bounce_group and (o := self.rect.collideobjects(list(self.bounce_group))):
            self.speed[0] *= -1

        super().update()

    
        
