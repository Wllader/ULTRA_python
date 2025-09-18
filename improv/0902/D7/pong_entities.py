import pygame as pg, numpy as np
from enum import Enum, auto

class MovingDirection(Enum):
    Horizontal  = auto()
    Vertical    = auto()


class PongEntity(pg.sprite.Sprite):
    def __init__(self,
                 screen:pg.Surface,
                 size:tuple[int],
                 init_center_pos:tuple[int],
                 speed:tuple[int],
                 color:tuple[int]
        ):
        super().__init__()

        self.size = np.array(size)
        self.speed = np.array(speed)
        self.color = np.array(color)

        self.screen = screen
        self._image = pg.Surface(size, pg.SRCALPHA)
        self._image.fill(self.color)

        self.rect = self._image.get_rect(center=np.array(init_center_pos))
        self.old_rect = self.rect.copy()


    @property
    def image(self):
        return self._image
    

    @property
    def screen_center(self):
        return np.array([
            self.screen.get_width(),
            self.screen.get_height()
        ]) / 2
    

    def update(self, dt):
        super().update()


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
        ...



class PongBot(PongEntity): #? Optional
    ...



class PongBall(PongEntity):
    def update(self, dt):
        ...

    def handle_collisions(self, direction:MovingDirection):
        ...

    def window_correction(self):
        super().window_correction()

        ...