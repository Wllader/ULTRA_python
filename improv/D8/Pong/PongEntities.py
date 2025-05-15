import pygame as pg, numpy as np
from abc import ABC
from GameController import GameController
from SpriteSheet import SpriteSheet


class PongEntity(pg.sprite.Sprite, ABC):
    def __init__(
            self, 
            screen:pg.Surface,
            size:np.ndarray,
            init_center_pos:np.ndarray,
            speed:np.ndarray,
            color:np.ndarray,
            sprite_sheet:SpriteSheet = None,
            *groups
        ):
        super().__init__(*groups)

        self.sheet = sprite_sheet
        self.screen = screen
        self.draw_func = pg.draw.rect
        self.image = pg.Surface(size)
        if sprite_sheet is not None:
            self.image = self.sheet.get_image(sprite_sheet.init_frame)
            self.draw_func = lambda **kwarg: ()

        self.rect = self.image.get_rect(center=init_center_pos)
        self.color = color
        self.speed = speed

        self.gc = GameController()

    @property
    def dt(self):
        return self.gc.dt

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value:np.ndarray):
        self._color = value
        if self.sheet:
            return
        self.image.fill((0, 0, 0, 0))
        self.draw_func(self.image, value, self.image.get_rect())

    def update(self):
        self.window_correction()

    def window_correction(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= (h := self.screen.get_height()):
            self.rect.bottom = h

        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= (w := self.screen.get_width()):
            self.rect.right = w

class PongPlayer(PongEntity):
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed[1] * self.dt
        if keys[pg.K_s]:
            self.rect.y += self.speed[1] * self.dt

        super().update()

class PongBot(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, sprite_sheet:SpriteSheet=None, *groups):
        self.ball:PongBall = None

        super().__init__(screen,
                         size, 
                         init_center_pos, 
                         speed, 
                         color,
                         sprite_sheet,
                         *groups)
    
    def update(self):
        #todo calculate exact location that the ball will hit
        #todo  and drift towards it with the paddle

        if self.ball and self.ball_moving_towards_me():
            self._drift_towards(self.ball.rect.center)
        else:
            h = self.screen.get_height() / 2
            self._drift_towards(np.array([0, h]))
        
        super().update()

    def ball_moving_towards_me(self) -> bool:
        ball_now = self.ball.rect.center
        ball_next = ball_now + self.ball.speed * self.dt

        dist_now = np.abs(self.rect.centerx - ball_now[0])
        dist_next = np.abs(self.rect.centerx - ball_next[0])

        return dist_next < dist_now


    def _drift_towards(self, center:np.ndarray):
        if self.rect.centery > center[1]:
                self.rect.y -= self.speed[1] * self.dt
        elif self.rect.centery < center[1]:
            self.rect.y += self.speed[1] * self.dt

    def _bounded(self):
        #todo might be useful to calculate the exact location
        #todo  using analytic geometry
        pass

class PongBotAdvanced(PongBot):
    def update(self):
        if self.ball_moving_towards_me():
            paddle_axis = 68 if self.ball.speed[0] < 0 else self.screen.get_width() - 68
            y = self.intersect(self.ball.speed, self.ball.rect.center, paddle_axis)
            y = self.bound(y, 0, self.screen.get_height())
            self._drift_towards(np.array([0, y]))
        else:
            center = np.array(self.screen.get_size()) / 2
            self._drift_towards(center)

        self.window_correction()

    def intersect(self, vector:np.ndarray, location:np.ndarray, axis_x):
        # ax + by + c = 0
        # c = -(ax + by): (-b, a) = ball.speed; (x, y) = ball.center
        # y = (ax + c)/(-b): (-b, a) = ball.speed; x = axis_x
        normal = vector.copy()[::-1]
        normal[0] *= -1

        c = -np.dot(normal, location)
        y = (normal[0]*axis_x + c)/(-normal[1])
        return y
    
    def bound(self, y:float, lower_bound:int, upper_bound:int) -> float:
        if y >= lower_bound and y <= upper_bound:
            return y
        
        if y < lower_bound:
            y0 = np.abs(lower_bound - y)
            return self.bound(y + 2*y0, lower_bound, upper_bound)
        
        if y > upper_bound:
            y0 = np.abs(upper_bound - y)
            return self.bound(y - 2*y0, lower_bound, upper_bound)

class PongBall(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, *groups):
        self.bounce_group:pg.sprite.Group = None
        self.default_color = color

        super().__init__(screen, size, init_center_pos, speed, color, *groups)
        self.draw_func = pg.draw.ellipse
        self.color = color

    def update(self):
        self.rect.x += self.speed[0] * self.dt
        self.rect.y += self.speed[1] * self.dt

        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height():
            self.speed[1] *= -1

        if (l := self.rect.left <= 0) or self.rect.right >= self.screen.get_width():
            self.speed[0] *= -1
            self.rect.centerx = self.screen.get_width() / 2
            self.rect.centery = np.random.randint(0, self.screen.get_height())
            self.color = self.default_color

            self.gc.score(1) if l else self.gc.score(0)

        if self.bounce_group and (o := self.rect.collideobjects(list(self.bounce_group))):
            self.speed[0] *= -1
            self.color = o.color

        super().update()

    
        
