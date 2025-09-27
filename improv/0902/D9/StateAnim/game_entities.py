import pygame as pg, numpy as np
from game_controller import GameController
from spritesheet_mr_d import SpriteSheet
from enum import Enum, auto

class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, size:tuple[int], init_pos:tuple[int]):
        super().__init__()

        self.screen = screen
        self._image = pg.Surface(size, pg.SRCALPHA)
        self._rect = self._image.get_rect(topleft=init_pos)

        self.gravity = 6

        self.gc = GameController()

    @property
    def image(self):
        self._image.fill((260, 100, 20))
        return self._image
    
    @property
    def rect(self):
        self._rect = self._image.get_rect(topleft = self._rect.topleft)
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
            self.rect.right = 0


class Dino(Entity):
    class State(Enum):
        Idle = auto()
        Walk = auto()

    class Direction(Enum):
        Right = 0
        Left = 1


    def __init__(self, screen, size, init_pos, spritesheet:SpriteSheet=None, speed:float= 5.):
        super().__init__(screen, size, init_pos)

        self.sheet = spritesheet
        self.speed = speed
        self.jmp_pwr = 150
        self.state = self.State.Idle
        self.direction = self.Direction.Right

        self.sheet.add_animation("idle", [ np.array([i, 0]) for i in range(4) ])
        self.sheet.add_animation("walk", [ np.array([i, 0]) for i in range(4, 10) ])


    @property
    def image(self):
        if self.sheet is None:
            self._image.fill((45, 212, 32))
        else:
            self._image = pg.transform.flip(self.sheet.frame, self.direction.value, 0).convert_alpha()

        return self._image

    @property
    def grounded(self):
        return self.rect.bottom == self.screen.get_height()


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

        if keys[pg.K_w] and self.grounded and self.state == self.State.Idle:
            self.rect.y -= self.jmp_pwr * self.dt


        #Gravity
        self.rect.y += self.gravity * self.dt

        self.sheet.set_animation(self.state.name)
        self.window_correction()