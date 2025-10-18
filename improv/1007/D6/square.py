import pygame as pg, numpy as np
from enum import Enum, auto


class MovingDirection(Enum):
    Horizontal = auto()
    Vertical = auto()


class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, init_pos:tuple[int], size:tuple[int], color:tuple[int] = (255, 255, 255)):
        super().__init__()

        self.screen = screen
        self.color = np.array(color)
        self.image = pg.Surface(size)
        self.image.fill(self.color)

        self.rect = self.image.get_rect(topleft=init_pos)
        self.old_rect = self.rect.copy()


    def update(self):
        super().update()


    def window_correction(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > (h := self.screen.get_height()):
            self.rect.bottom = h

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > (w := self.screen.get_width()):
            self.rect.right = w


class Square(Entity):
    def __init__(self, screen, init_pos, size, color = (200, 180, 30), speed:tuple[int]=None):
        super().__init__(screen, init_pos, size, color)

        self.speed = np.array(speed) if speed else np.array((5, 5))
        self.collison_group = pg.sprite.Group()
    
    def handle_collisions(self, direction:MovingDirection) -> np.ndarray:
        if o := self.rect.collideobjects(list(self.collison_group)):
            o:Entity
            
            match direction:
                case MovingDirection.Horizontal:
                    if self.rect.left <= o.rect.right and self.old_rect.left > o.rect.right:
                        self.rect.left = o.rect.right
                        return np.array([-1, 1])
                    elif self.rect.right >= o.rect.left and self.old_rect.right < o.rect.left:
                        self.rect.right = o.rect.left
                        return np.array([-1, 1])

                case MovingDirection.Vertical:
                    if self.rect.top <= o.rect.bottom and self.old_rect.top > o.rect.bottom:
                        self.rect.top = o.rect.bottom
                        return np.array([1, -1])
                    elif self.rect.bottom >= o.rect.top and self.old_rect.bottom < o.rect.top:
                        self.rect.bottom = o.rect.top
                        return np.array([1, -1])
                    
        return np.array([1, 1])
                    

    def update(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.rect.x += self.speed[0] * dt
        if keys[pg.K_a]:
            self.rect.x -= self.speed[0] * dt
        self.speed *= self.handle_collisions(MovingDirection.Horizontal)

        if keys[pg.K_w]:
            self.rect.y -= self.speed[1] * dt
        if keys[pg.K_s]:
            self.rect.y += self.speed[1] * dt
        self.speed *= self.handle_collisions(MovingDirection.Vertical)

        self.window_correction()
        self.old_rect = self.rect.copy()


class PlayerSquare(Square):
    pass



class MovingSquare(Square):
    pass
