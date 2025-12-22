import pygame as pg, numpy as np
from game_controller import GameController
from spritesheet_mr_d import SpriteSheet
from enum import Enum, auto

class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, size:tuple[int], init_pos:tuple[int], spritesheet:SpriteSheet=None):
        super().__init__()

        self.screen = screen
        self.sheet = spritesheet
        self._image = pg.Surface(size, pg.SRCALPHA)
        self._rect = self._image.get_rect(topleft=init_pos)
        self.gravity = 6

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
        elif self.rect.bottom > (h := self.screen.height):
            self.rect.bottom = h

        w = self.screen.width
        if self.rect.right < 0:
            self.rect.left = w
        elif self.rect.left > w:
            self.rect.right = 0

class Dino(Entity):
    class State(Enum):
        Idle = auto()
        Walk = auto()

    class Direction(Enum):
        Right = 0
        Left = 1

    def __init__(self, screen, size, init_pos, spritesheet = None, speed:float=6.):
        super().__init__(screen, size, init_pos, spritesheet)

        self.speed = speed
        self.state = self.State.Idle
        self.direction = self.Direction.Right

        self.sheet.add_animation("idle", [ np.array([i, 0]) for i in range(4) ])
        self.sheet.add_animation("walk", [ np.array([i, 0]) for i in range(4, 10) ])
        self.sheet.set_animation("idle", 150)

    @property
    def image(self):
        if self.sheet is None:
            self._image.fill((45, 212, 32))
        else:
            self._image = pg.transform.flip(self.sheet.frame, self.direction.value, 0)

        return self._image

    def update(self):
        self.state = self.State.Idle

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -= self.speed * self.dt
            self.state = self.State.Walk
            self.direction = self.Direction.Left

        if keys[pg.K_d]:
            self.rect.x += self.speed * self.dt
            self.state = self.State.Walk
            self.direction = self.Direction.Right

        self.rect.y += self.gravity * self.dt

        self.sheet.set_animation(self.state.name)
        self.window_correction()