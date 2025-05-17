import pygame as pg, numpy as np
from GameController import GameController
from SpriteSheet import SpriteSheet
from enum import Enum, auto


class MovingDirection(Enum):
    Horizontal = auto()
    Vertical = auto()

class Entity(pg.sprite.Sprite):
    def __init__(
            self,
            screen:pg.Surface,
            init_center_pos:np.ndarray,
            sprite_sheet:SpriteSheet
    ):
        super().__init__()

        self.screen = screen
        self.sheet = sprite_sheet

        self._image = sprite_sheet.frame
        self.rect = self._image.get_rect(center=init_center_pos)

        self.old_rect = self.rect.copy()
        self.gc = GameController()

    @property
    def dt(self):
        return self.gc.dt
    
    @property
    def image(self):
        return self.sheet.frame
    

    def update(self):
        self.window_correction()

        # self._image = self.sheet.frame
        self.old_rect = self.rect.copy()

    def window_correction(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= (h := self.screen.get_height()):
            self.rect.bottom = h

        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= (w := self.screen.get_width()):
            self.rect.right = w

class Dinosaur(Entity):
    def __init__(
            self,
            screen,
            init_center_pos,
            sprite_sheet,
            speed,
            collision_group = None
    ):
        super().__init__(screen, init_center_pos, sprite_sheet)

        self.speed = speed
        self.current_vert_speed = 0
        self.jump_power = 5

        self.collisions = collision_group
        self.g = 3

        self.current_acc = np.zeros(4) #l, r, u, d
        self.current_speed = np.zeros(4) #l, r, u, d

    def update(self):
        keys = pg.key.get_pressed()
        current_horiz_speed = (self.speed if keys[pg.K_d] else 0) - (self.speed if keys[pg.K_a] else 0)
        current_vert_acc = self.jump_power if keys[pg.K_w] else 0

        self.current_vert_speed += np.clip(self.g - current_vert_acc, -1, 10)

        self.rect.centerx += current_horiz_speed * self.dt
        self.collision(MovingDirection.Horizontal)

        self.rect.centery += self.current_vert_speed * self.dt
        self.collision(MovingDirection.Vertical)


        super().update()

    def collision(self, direction:MovingDirection):
        if self.collisions is None: return
        if o := self.rect.collideobjects(list(self.collisions)):
            o:Entity
            if direction == MovingDirection.Horizontal:
                if self.rect.left <= o.rect.right and self.old_rect.left >= o.rect.right:
                    # self.rect.left = o.rect.right
                    o.rect.right = self.rect.left
                elif self.rect.right > o.rect.left and self.old_rect.right <= o.rect.left:
                    # self.rect.right = o.rect.left
                    o.rect.left = self.rect.right

            elif direction == MovingDirection.Vertical:
                if self.rect.bottom >= o.rect.top and self.old_rect.bottom <= o.rect.top:
                    self.rect.bottom = o.rect.top
                elif self.rect.top <= o.rect.bottom and self.old_rect.top >= o.rect.bottom:
                    self.rect.top = o.rect.bottom
