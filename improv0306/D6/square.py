import pygame as pg, numpy as np

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, init_pos:np.ndarray, size:np.ndarray, color:np.random = WHITE):
        super().__init__()

        self.screen = screen
        self.image = pg.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=init_pos)
        self.color = color

    def update(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > (h := self.screen.get_height()):
            self.rect.bottom = h

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > (w := self.screen.get_width()):
            self.rect.right = w

    
class Square(Entity):
    def __init__(self, screen, init_pos, size, color = WHITE, speed:np.ndarray = np.array([5, 5])):
        super().__init__(screen, init_pos, size, color)

        self.speed = speed

    def update(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -= self.speed[0] * dt
        if keys[pg.K_d]:
            self.rect.x += self.speed[0] * dt
        if keys[pg.K_w]:
            self.rect.y -= self.speed[1] * dt
        if keys[pg.K_s]:
            self.rect.y += self.speed[1] * dt

        super().update()


class Moving_Square(Entity):
    