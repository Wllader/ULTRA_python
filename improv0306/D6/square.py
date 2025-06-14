import pygame as pg, numpy as np
from enum import Enum, auto
from game_controller import GameController

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

class MovingDirection(Enum):
    Horizontal = auto()
    Vertical = auto()


class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, init_pos:np.ndarray, size:np.ndarray, color:np.random = WHITE):
        super().__init__()

        self.gc = GameController()
        self.screen = screen
        self.color = color
        self._image = pg.Surface(size)
        self._rect = self.image.get_rect(topleft=init_pos)

        self.old_rect = self.rect.copy()

    @property
    def image(self):
        self._image.fill(self.color)
        return self._image
    
    @property
    def rect(self):
        return self._rect
    
    @rect.setter
    def rect(self, value):
        self._rect = value

    @property
    def dt(self):
        return self.gc.dt


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
    
class Square(Entity):
    def __init__(self, screen, init_pos, size, color = WHITE, speed:np.ndarray = np.array([5, 5])):
        super().__init__(screen, init_pos, size, color)

        self.collission_group = pg.sprite.Group()
        self.speed = speed

        self.space_held = False

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -= self.speed[0] * self.dt
        if keys[pg.K_d]:
            self.rect.x += self.speed[0] * self.dt
        self.handle_collissions(MovingDirection.Horizontal)

        if keys[pg.K_w]:
            self.rect.y -= self.speed[1] * self.dt
        if keys[pg.K_s]:
            self.rect.y += self.speed[1] * self.dt
        self.handle_collissions(MovingDirection.Vertical)

        if (space := keys[pg.K_SPACE]) and not self.space_held:
            self.color = np.random.randint(0, 256, 3)
            self.space_held = True
        elif not space:
            self.space_held = False
            

        self.window_correction()

        self.old_rect = self.rect.copy()

    def handle_collissions(self, direction:MovingDirection) -> np.ndarray:
        if (o := self.rect.collideobjects(list(self.collission_group))) and o is not None:
            o:Entity

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
                


class Moving_Square(Square):
    def __init__(self, screen, init_pos, size, color=WHITE, speed = np.array([0, 5])):
        super().__init__(screen, init_pos, size, color, speed)

    def update(self):
        self.rect.x += self.speed[0] * self.dt
        self.speed *= self.handle_collissions(MovingDirection.Horizontal)

        self.rect.y += self.speed[1] * self.dt
        self.speed *= self.handle_collissions(MovingDirection.Vertical)

        if self.rect.left <= 0 or self.rect.right >= self.screen.get_width():
            self.speed[0] *= -1

        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height():
            self.speed[1] *= -1


        self.window_correction()

        self.old_rect = self.rect.copy()
