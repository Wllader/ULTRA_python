import pygame as pg, numpy as np
from abc import ABC
from enum import Enum, auto
from game_controller import GameController
from sprite_sheet import SpriteSheet

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
            color:np.ndarray,
            sprite_sheet:SpriteSheet = None
        ):
        super().__init__()

        self.gc = GameController()
        
        self.sheet = sprite_sheet if sprite_sheet else None
        self.screen = screen
        self._image = pg.Surface(size)
        if sprite_sheet is not None:
            self._image = self.sheet.frame

        self.color = color
        self.rect = self.image.get_rect(center=init_center_pos)
        self.speed = speed

        self.old_rect = self.rect.copy()

    @property
    def dt(self):
        return self.gc.dt
    
    @property
    def screen_center(self):
        return np.array([
                self.screen.get_width(),
                self.screen.get_height()
            ]) / 2

    @property
    def image(self):
        if self.sheet is None:
            self._image.fill(self.color)
        else:
            self._image = self.sheet.frame #new
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

    @staticmethod
    def intersect(vector:np.ndarray, location:np.ndarray, axis_x) -> float:
        # ax + by + c = 0
        # c = -(ax + by): (-b, a) = ball_speed, (x, y) = ball_center
        # y = (ax + c)/(-b): (-b, a) = ball_speed, x = axis_x
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
        # a := start, b := end
        # (1-t)*a + t*b = axis
        # (1-t)*a_y + t*b_y = axis_y
        # -> t = (axis-a)/(b-a)
        
        t = ((axis - start)/(end - start))[index]

        return (1-t)*start + t*end, t


class PongPlayer(PongEntity):
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed[1] * self.dt

        if keys[pg.K_s]:
            self.rect.y += self.speed[1] * self.dt

        self.window_correction()

class PongBot(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, sprite_sheet:SpriteSheet):
        super().__init__(screen, size, init_center_pos, speed, color, sprite_sheet)

        self.target:PongEntity = None

    def update(self):
        if self.target is None: return
        if self.ball_moving_towards_me():
            self.drift_towards(self.target.rect.center)
        else:
            self.drift_towards(self.screen_center)

        self.window_correction()

    def drift_towards(self, center:np.ndarray):
        if self.rect.centery > center[1]:
            self.rect.y -= self.speed[1] * self.dt
        elif self.rect.centery < center[1]:
            self.rect.y += self.speed[1] * self.dt

    def ball_moving_towards_me(self) -> bool:
        ball_now = self.target.rect.center
        ball_next = ball_now + self.target.speed * self.dt

        dist_now = np.abs(self.rect.centerx - ball_now[0])
        dist_next = np.abs(self.rect.centerx - ball_next[0])

        return dist_next < dist_now


class PongBotAdvanced(PongBot):
    def update(self):
        if self.ball_moving_towards_me():
            paddle_axis = 68 if self.target.speed[0] < 0 else self.screen.get_width() - 68
            y = self.intersect(self.target.speed, self.target.rect.center, paddle_axis)
            y = self.bound(y, 0, self.screen.get_height())
            self.drift_towards(np.array([0, y]))
        else:
            self.drift_towards(self.screen_center)


        self.window_correction()
        self.old_rect = self.rect.copy()


class PongBall(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, sprite_sheet:SpriteSheet):
        super().__init__(screen, size, init_center_pos, speed, color, sprite_sheet)

        self.g_bounce = pg.sprite.Group()

    @property
    def image(self):
        if self.sheet is None:
            pg.draw.ellipse(self._image, self.color, self._image.get_rect())
        else:
            self._image = self.sheet.frame #new
        return self._image


    def update(self):
        self.rect.x += self.speed[0] * self.dt
        self.handle_collisions(MovingDirection.Horizontal)

        self.rect.y += self.speed[1] * self.dt
        self.handle_collisions(MovingDirection.Vertical)

        self.window_correction()

        self.old_rect = self.rect.copy()

    def handle_collisions(self, direction:MovingDirection):
        if (o := self.rect.collideobjects(list(self.g_bounce))) and o is not None:
            o:PongEntity

            self.color = o.color

            if direction == MovingDirection.Horizontal:
                if self.rect.left <= o.rect.right and self.old_rect.left >= o.rect.right:
                    self.bounce(o.rect.right + self.rect.width / 2, 0)
                elif self.rect.right >= o.rect.left and self.old_rect.right <= o.rect.left:
                    self.bounce(o.rect.left - self.rect.width / 2, 0)
                

            if direction == MovingDirection.Vertical:
                if self.rect.top <= o.rect.bottom and self.old_rect.top >= o.rect.bottom:
                    self.bounce(o.rect.bottom + self.rect.height / 2, 1)
                elif self.rect.bottom >= o.rect.top and self.old_rect.bottom <= o.rect.top:
                    self.bounce(o.rect.top - self.rect.height / 2, 1)

    
    def window_correction(self):
        super().window_correction()

        if self.rect.top <= 0:
            self.bounce(0 + self.rect.height / 2, 1)
        elif self.rect.bottom >= (h := self.screen.get_height()):
            self.bounce(h - self.rect.height / 2, 1)

        #? Respawn
        if self.rect.left <= 0 or self.rect.right >= self.screen.get_width():
            self.rect.center = np.array([
                self.screen_center[0],
                np.random.randint(0, self.screen.get_height())
            ])
            self.color = np.ones(3, dtype=np.uint8) * 255
            self.speed[0] *= -1

    def bounce(self, axis:float, index:int):
        c, t = self.ccd(
            np.array(self.old_rect.center), np.array(self.rect.center),
            axis, index
        )

        self.speed[index] *= -1
        self.rect.center = c + self.speed[index] * (1-t)