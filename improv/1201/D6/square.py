import pygame as pg, numpy as np


class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, init_pos:tuple[int], size:tuple[int], color:tuple[int] = (255, 255, 255)):
        super().__init__()

        self.screen = screen
        self.color = np.array(color)
        self.image = pg.Surface(size)
        self.image.fill(self.color)

        self.rect = self.image.get_frect(topleft=init_pos)

    def update(self, dt):
        super().update()

    def window_correction(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > (h := self.screen.height):
            self.rect.bottom = h

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > (w := self.screen.width):
            self.rect.right = w


class Square(Entity):
    def __init__(self, screen, init_pos, size, color = (255, 255, 255), speed:tuple[int]=None):
        super().__init__(screen, init_pos, size, color)

        self.speed = np.array(speed) if speed else np.array([5, 5])


    def update(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rect.x += self.speed[0] * dt
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rect.x -= self.speed[0] * dt
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.rect.y -= self.speed[1] * dt
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.rect.y += self.speed[1] * dt

        self.window_correction()

class MovingSquare(Square):
    ...


class PlayerSquare(Square):
    ...
    