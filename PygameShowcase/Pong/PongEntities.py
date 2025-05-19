import pygame as pg, numpy as np
from typing import override
from abc import ABC
from SpriteSheet import SpriteSheet
from GameController import GameController

from enum import Enum, auto

class PongEntity(pg.sprite.Sprite, ABC):
    def __init__(
            self,
            screen:pg.Surface,
            size:np.ndarray,
            init_center_pos:np.ndarray,
            speed:np.ndarray,
            color:tuple,
            sprite_sheet:SpriteSheet = None,
            *groups
        ):
        super().__init__(*groups)
        self.screen = screen
        self.sheet = sprite_sheet

        if sprite_sheet:
            self.image = sprite_sheet.frame
            self.draw_func = lambda **kwargs: ()
            self._color = (0, 0, 0, 0)

        else:
            self.image = pg.Surface(size)
            self.draw_func = pg.draw.rect
            self.color = color
            

        self.rect = self.image.get_rect(center=init_center_pos)
        self.old_rect = self.rect.copy()

        self.speed = speed
        self.gc = GameController()

    @property
    def dt(self):
        return self.gc.dt

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if self.sheet:
            return
        self._color = color
        self.image.fill((0, 0, 0, 0))
        self.draw_func(self.image, color, self.image.get_rect())

    
    def update(self):
        self.window_correction()

        self.image = self.sheet.frame
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

    @staticmethod
    def intersect(vector:np.ndarray, location:np.ndarray, axis_x):
        # ax + by + c = 0
        # c = -(ax + by): (-b, a) = ball.speed; (x, y) = ball.center
        # y = (ax + c)/(-b): (-b, a) = ball.speed; (x, y) = point on axis
        normal = vector.copy()[::-1]
        normal[0] *= -1
        c = -np.dot(normal, location)
        y = (normal[0] * axis_x + c)/(-normal[1])
        return y

    @staticmethod
    def bound(y:float, lower_bound:int, upper_bound:int) -> float:
        if y >= lower_bound and y <= upper_bound:
            return y

        if y < lower_bound:
            y0 = np.abs(lower_bound - y)
            return PongEntity.bound(y + 2*y0, lower_bound, upper_bound)
        
        if y > upper_bound:
            y0 = np.abs(upper_bound - y)
            return PongEntity.bound(y - 2*y0, lower_bound, upper_bound)

    @staticmethod
    def ccd(start:np.ndarray, end:np.ndarray, axis:float, index:int) -> tuple[np.ndarray, float]:
        # a := end, b := start
        # a*t + b*(1-t) = axis
        # a[1]*t + b[1]*(1-t) = axis_y
        # -> t = (axis-b)/(a-b)
        t = ((axis - start)/(end - start))[index]

        return start * t + end * (1-t), t


class PongPlayer(PongEntity):    
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed[1] * self.dt
        if keys[pg.K_s]:
            self.rect.y += self.speed[1] * self.dt

        super().update()

class PongBot(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, sprite_sheet=None, *groups):
        self.ball:PongBall = None

        super().__init__(screen, size, init_center_pos, speed, color, sprite_sheet, *groups)

    
    def update(self):
        if self.ball:
            ball_pos = self.ball.rect.center
            ball_next_pos = ball_pos + self.ball.speed * self.dt

            if np.abs(self.rect.center[0] - ball_pos[0]) > np.abs(self.rect.center[0] - ball_next_pos[0]):
                self.drift_towards(self.ball.rect.center)
                return

        center = np.array(self.screen.get_size()) / 2
        self.drift_towards(center)

        super().update()

    def drift_towards(self, position):
        if self.rect.centery > position[1]:
            self.rect.y -= self.speed[1] * self.dt
        elif self.rect.centery < position[1]:
            self.rect.y += self.speed[1] * self.dt

class PongBotAdvanced(PongBot):
    def update(self):
        if self.ball_moving_towards_me():
            paddle_axis = (55 + 8) if self.ball.speed[0] < 0 else self.screen.get_width() - (55 + 8)
            y = self.intersect(self.ball.speed, self.ball.rect.center, paddle_axis)
            y = self.bound(y, 0, self.screen.get_height())
            self.drift_towards(np.array([0, int(y)]))
        else:
            center = np.array(self.screen.get_size()) / 2
            self.drift_towards(center)

        self.window_correction()
        self.image = self.sheet.frame

    def ball_moving_towards_me(self) -> bool:
        ball_pos_now = self.ball.rect.center
        ball_pos_next = ball_pos_now + self.ball.speed * self.dt

        distance_now = np.abs(self.rect.center[0] - ball_pos_now[0])
        distance_next = np.abs(self.rect.center[0] - ball_pos_next[0])

        return distance_next < distance_now



class PongBall(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, sprite_sheet=None, *groups):
        self.bounce_group:pg.sprite.Group = None

        super().__init__(screen, size, init_center_pos, speed, color, sprite_sheet, *groups)
        self.draw_func = pg.draw.ellipse
        self.color = color

    
    def update(self):
        self.rect.x += self.speed[0] * self.dt
        self.collision(MovingDirection.Horizontal)

        self.rect.y += self.speed[1] * self.dt
        self.collision(MovingDirection.Vertical)

        self.window_collision()
        super().update()

    def collision(self, direction:"MovingDirection"):
        if o := self.rect.collideobjects(list(self.bounce_group)):
            o:"PongEntity"
            self.color = o.color

            if direction == MovingDirection.Horizontal:
                if self.rect.left <= o.rect.right and self.old_rect.left >= o.rect.right:
                    self.bounce(o.rect.right + self.rect.width / 2, 0)
                elif self.rect.right > o.rect.left and self.old_rect.right <= o.rect.left:
                    self.bounce(o.rect.left - self.rect.width / 2, 0)

            elif direction == MovingDirection.Vertical:
                if self.rect.bottom >= o.rect.top and self.old_rect.bottom <= o.rect.top:
                    self.bounce(o.rect.top - self.rect.height / 2, 1)
                elif self.rect.top <= o.rect.bottom and self.old_rect.top >= o.rect.bottom:
                    self.bounce(o.rect.bottom + self.rect.height / 2, 1)


    def window_collision(self):
        if self.rect.top <= 0:
            self.bounce(0 + self.rect.height / 2, 1)
        elif self.rect.bottom >= (h := self.screen.get_height()):
            self.bounce(h - self.rect.height / 2, 1)
        
        #? Score & Respawn:
        if (l := self.rect.left <= 0) or self.rect.right >= self.screen.get_width():
            self.speed[0] *= -1
            self.rect.center = self.screen.get_width() / 2, np.random.randint(0, self.screen.get_height())
            self.color = (255, 255, 255)

            self.gc.score(0) if not l else self.gc.score(1)

    def bounce(self, axis:float, index:int):
        c, t = self.ccd(
            np.array(self.old_rect.center), np.array(self.rect.center),
            axis, index
        )

        self.speed[index] *= -1
        return c + (1 - t) * self.speed[index]


class MovingDirection(Enum):
    Horizontal = auto()
    Vertical = auto()
            
if __name__ == "__main__":
    print(PongEntity.ccd(np.array([1, 1]), np.array([1, -1]), np.array([0, 0.5]), index=1))