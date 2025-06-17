import pygame as pg, numpy as np
from abc import ABC
from enum import Enum, auto
from game_controller import GameController

class MovingDirection(Enum):
    Horizontal = auto()
    Vertical = auto()

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

        self.gc = GameController()

        self.screen = screen
        self._image = pg.Surface(size)
        self.color = color
        self.rect = self.image.get_rect(center=init_center_pos)
        self.speed = speed

        self.old_rect = self.rect.copy()

    @property
    def dt(self):
        return self.gc.dt

    @property
    def image(self):
        self._image.fill(self.color)
        return self._image

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
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed[1] * self.dt

        if keys[pg.K_s]:
            self.rect.y += self.speed[1] * self.dt

        self.window_correction()

class PongBot(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color):
        super().__init__(screen, size, init_center_pos, speed, color)

        self.target:PongEntity = None

    def update(self):
        if self.target is None: return
        self.drift_towards(self.target.rect.center)

        self.window_correction()

    def drift_towards(self, center:np.ndarray):
        if self.rect.centery > center[1]:
            self.rect.y -= self.speed[1] * self.dt
        elif self.rect.centery < center[1]:
            self.rect.y += self.speed[1] * self.dt


class PongBall(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color):
        super().__init__(screen, size, init_center_pos, speed, color)

        self.g_bounce = pg.sprite.Group()

    @property
    def image(self):
        pg.draw.ellipse(self._image, self.color, self._image.get_rect())
        return self._image


    def update(self):
        self.rect.x += self.speed[0] * self.dt
        self.speed *= self.handle_collisions(MovingDirection.Horizontal)

        self.rect.y += self.speed[1] * self.dt
        self.speed *= self.handle_collisions(MovingDirection.Vertical)

        self.window_correction()

        self.old_rect = self.rect.copy()

    def handle_collisions(self, direction:MovingDirection) -> np.ndarray:
        if (o := self.rect.collideobjects(list(self.g_bounce))) and o is not None:
            o:PongEntity

            self.color = o.color

            if direction == MovingDirection.Horizontal:
                if self.rect.left <= o.rect.right and self.old_rect.left >= o.rect.right:
                    self.rect.left = o.rect.right
                    return np.array([-1, 1])
                elif self.rect.right >= o.rect.left and self.old_rect.right <= o.rect.left:
                    self.rect.right = o.rect.left
                    return np.array([-1, 1])
                

            if direction == MovingDirection.Vertical:
                if self.rect.top <= o.rect.bottom and self.old_rect.top >= o.rect.bottom:
                    self.rect.top = o.rect.bottom
                    return np.array([1, -1])
                elif self.rect.bottom >= o.rect.top and self.old_rect.bottom <= o.rect.top:
                    self.rect.bottom = o.rect.top
                    return np.array([1, -1])
                
        return np.ones(2, dtype=int)
    

    @property
    def screen_center(self):
        return np.array([
                self.screen.get_width(),
                self.screen.get_height()
            ]) / 2
    
    def window_correction(self):
        super().window_correction()

        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height():
            self.speed[1] *= -1

        if self.rect.left <= 0 or self.rect.right >= self.screen.get_width():
            self.rect.center = self.screen_center
            self.color = np.ones(3, dtype=np.uint8) * 255
            self.speed[0] *= -1