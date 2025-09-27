import pygame as pg, numpy as np
from enum import Enum, auto
from game_controller import GameController
from spritesheet_sr_fc import SpriteSheet


GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

class MovingDirection(Enum):
    Horizontal  = auto()
    Vertical    = auto()


class PongEntity(pg.sprite.Sprite):
    def __init__(self,
                 screen:pg.Surface,
                 size:tuple[int],
                 init_center_pos:tuple[int],
                 speed:tuple[int],
                 color:tuple[int],
                 spritesheet:SpriteSheet = None
        ):
        super().__init__()
        self.gc = GameController()
        self.sheet = spritesheet

        self.size = np.array(size)
        self.speed = np.array(speed)

        self.screen = screen
        self._image = pg.Surface(size, pg.SRCALPHA)
        self.color = np.array(color)
        self._image.fill(self.color)

        self.rect = self._image.get_rect(center=np.array(init_center_pos))
        self.old_rect = self.rect.copy()



    @property
    def dt(self):
        return self.gc.dt

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value:tuple[int]):
        self._color = np.array(value)
        if self.sheet is None:
            self._image.fill(self.color)

    @property
    def image(self):
        if self.sheet:
            self._image = self.sheet.frame
        return self._image

    @property
    def screen_center(self):
        return np.array([
            self.screen.get_width(),
            self.screen.get_height()
        ]) / 2
    

    def update(self):
        super().update()


    def window_correction(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > (h := self.screen.get_height()):
            self.rect.bottom = h

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > (w := self.screen.get_width()):
            self.rect.right = w



class PongPlayer(PongEntity):
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.rect.y -= self.speed[1] * self.dt
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.rect.y += self.speed[1] * self.dt

        self.window_correction()
        self.old_rect = self.rect.copy()



class PongBot(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, spritesheet):
        super().__init__(screen, size, init_center_pos, speed, color, spritesheet)

        self.ball:PongEntity = None

    def update(self):
        if self.ball is None: return

        if self.ball_moving_towards_me():
            self.drift_towards(self.ball.rect.center)
        else:
            self.drift_towards(self.screen_center)

        self.window_correction()

    def drift_towards(self, center:tuple):
        if self.rect.centery > center[1]:
            self.rect.y -= self.speed[1] * self.dt
        elif self.rect.centery < center[1]:
            self.rect.y += self.speed[1] * self.dt

    def ball_moving_towards_me(self) -> bool:
        ball_now = self.ball.rect.center
        ball_next = ball_now + self.ball.speed * self.dt

        dist_now = np.abs(self.rect.centerx - ball_now[0])
        dist_next = np.abs(self.rect.centerx - ball_next[0])

        return dist_next < dist_now


class PongBotAdvanced(PongBot):
    def update(self):
        if self.ball_moving_towards_me():
            ball_half_width = self.ball.rect.width / 2
            paddle_axis = self.rect.right + ball_half_width if self.ball.speed[0] < 0 else self.rect.left - ball_half_width
            y = self.intersect(self.ball.speed, self.ball.rect.center, paddle_axis)
            y = self.bound(y, 0, self.screen.get_height())
            self.drift_towards(np.array((paddle_axis, y), dtype=int))

        else:
            self.drift_towards(self.screen_center)

        self.window_correction()
        self.old_rect = self.rect.copy()


    @staticmethod
    def intersect(vector:np.ndarray, location:np.ndarray, axis_x) -> float:
        # ax + by + c = 0
        # c = -(ax + by): (-b, a)=target_speed, (x, y)=target_center
        # y = (ax + c)/(-b): (-b, a)=target_speed, x=axis_x
        normal = vector.copy()[::-1]
        normal[0] *= -1

        c = -np.dot(normal, location)
        y:float = (normal[0] * axis_x + c)/(-normal[1])

        return y
        


    @staticmethod
    def bound(y:float, lower_bound:int, upper_bound:int) -> float:
        if y >= lower_bound and y <= upper_bound:
            return y
        
        if y < lower_bound:
            y0 = np.abs(lower_bound - y)
            return PongBotAdvanced.bound(y + 2*y0, lower_bound, upper_bound)
        
        if y > upper_bound:
            y0 = np.abs(upper_bound - y)
            return PongBotAdvanced.bound(y - 2*y0, lower_bound, upper_bound)


class PongBall(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, spritesheet):
        super().__init__(screen, size, init_center_pos, speed, color, spritesheet)

        self._image.fill((0, 0, 0, 0))
        pg.draw.ellipse(self._image, self.color, self._image.get_rect())

        self.g_bounce = pg.sprite.Group()

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value:tuple[int]):
        self._color = np.array(value)
        if self.sheet is None:
            self._image.fill((0, 0, 0, 0))
            pg.draw.ellipse(self._image, self.color, self._image.get_rect())

    def update(self):
        self.rect.x += self.speed[0] * self.dt
        self.speed *= self.handle_collisions(MovingDirection.Horizontal)

        self.rect.y += self.speed[1] * self.dt
        self.speed *= self.handle_collisions(MovingDirection.Vertical)

        self.window_correction()
        self.old_rect = self.rect.copy()


    def handle_collisions(self, direction:MovingDirection):
        if o := self.rect.collideobjects(list(self.g_bounce)):
            o:PongEntity

            self.color = o.color

            match direction:
                case MovingDirection.Horizontal:
                    if self.rect.left <= o.rect.right and self.old_rect.left >= o.rect.right:
                        self.rect.left = o.rect.right
                        return np.array([-1, 1])
                    elif self.rect.right >= o.rect.left and self.old_rect.right <= o.rect.left:
                        self.rect.right = o.rect.left
                        return np.array([-1, 1])

                case MovingDirection.Vertical:
                    if self.rect.top <= o.rect.bottom and self.old_rect.top >= o.rect.bottom:
                        self.rect.top = o.rect.bottom
                        return np.array([1, -1])
                    elif self.rect.bottom >= o.rect.top and self.old_rect.bottom <= o.rect.top:
                        self.rect.bottom = o.rect.top
                        return np.array([1, -1])

        return 1

    def window_correction(self):
        super().window_correction()

        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height():
            self.speed[1] *= -1

        if (l := self.rect.left <= 0) or self.rect.right >= self.screen.get_width():
            self.speed[0] *= -1
            self.rect.center = (
                self.screen_center[0],
                np.random.randint(self.rect.height + 5, self.screen.get_height() - (self.rect.height + 5))
            )
            self.color = WHITE
            
            self.gc.score(1) if l else self.gc.score(0)