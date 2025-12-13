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

        self.rect = self.image.get_frect(topleft=init_pos)
        self.old_rect = self.rect.copy()

        self.collision_group = pg.sprite.Group()

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

    def handle_collisions(self, direction:MovingDirection) -> np.ndarray:
        if o := self.rect.collideobjects(list(self.collision_group)):
            o:Entity

            match direction:
                case MovingDirection.Horizontal:
                    dx = self.rect.x - self.old_rect.x

                    if dx > 0: #Right
                        self.rect.right = o.rect.left
                        return np.array([-1, 1]) 
                    elif dx < 0: #Left
                        self.rect.left = o.rect.right
                        return np.array([-1, 1]) 


                case MovingDirection.Vertical:
                    dy = self.rect.y - self.old_rect.y

                    if dy > 0: #Down
                        self.rect.bottom = o.rect.top
                        return np.array([1, -1])    
                    elif dy < 0: #Up
                        self.rect.top = o.rect.bottom
                        return np.array([1, -1])    

                                 
        return np.array([1, 1])


class Square(Entity):
    pass

class MovingSquare(Square):
    def __init__(self, screen, init_pos, size, color = (255, 255, 255), speed:tuple[int]=None):
        super().__init__(screen, init_pos, size, color)

        self.speed = np.array(speed) if speed else np.array([5, 5])

    def update(self, dt):
        self.rect.x += self.speed[0] * dt
        self.speed *= self.handle_collisions(MovingDirection.Horizontal)
        
        self.rect.y += self.speed[1] * dt
        self.speed *= self.handle_collisions(MovingDirection.Vertical)

        self.window_correction()
        self.window_collision()

        self.old_rect = self.rect.copy()

    def window_collision(self):
        if self.rect.top <= 0 or self.rect.bottom >= self.screen.height:
            self.speed[1] *= -1

        if self.rect.left <= 0 or self.rect.right >= self.screen.width:
            self.speed[0] *= -1



class PlayerSquare(MovingSquare):
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

        self.old_rect = self.rect.copy()
    