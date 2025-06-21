import pygame as pg, numpy as np
from game_controller import GameController
from spritesheet_mr_d import SpriteSheet
from enum import Enum, auto

class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, size:np.ndarray, init_pos:np.ndarray):
        super().__init__()

        self.screen = screen
        self._image = pg.Surface(size)
        self.rect = self.image.get_rect(topleft=init_pos)
        self.gravity = 10

        self.gc = GameController()

    @property
    def image(self):
        self._image.fill((160, 100, 20))
        return self._image
    
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
    class DinoState(Enum):
        Idle = auto()
        Walk = auto()

    class DinoDirection(Enum):
        Right = 0
        Left = 1

    def __init__(self, screen, size, init_pos, spritesheet:SpriteSheet = None, speed:float=5., jmp_pwr:float=150):
        #todo Better phisics - Accel based
        self.sheet = spritesheet
        self.speed = speed
        self.jmp_pwr = jmp_pwr
        self.state = self.DinoState.Idle
        self.direction = self.DinoDirection.Right

        super().__init__(screen, size, init_pos)

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
        self.state = self.DinoState.Idle

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -= self.speed * self.dt
            self.state = self.DinoState.Walk
            self.direction = self.DinoDirection.Left
        if keys[pg.K_d]:
            self.rect.x += self.speed * self.dt
            self.state = self.DinoState.Walk
            self.direction = self.DinoDirection.Right

        if keys[pg.K_w] and self.grounded:
            self.rect.y -= self.jmp_pwr * self.dt

        # Gravity
        self.rect.y += self.gravity * self.dt

        self.sheet.set_animation(self.state.name.lower())
        self.window_correction()