import pygame as pg, numpy as np
from enum import Enum, auto
from game_controller import GameController
from spritesheet_sr_fc import SpriteSheet

#Todo vytvořit základní PongEntity
#Todo Odvodit od ní PongPlayer, PongBot a PongBall objekty a implementovat jejich základní chování

class MovingDirection(Enum):
    Horizontal = auto()
    Vertical = auto()


class PongEntity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, size:tuple[int], init_center_pos:tuple[int], speed:tuple[int], color:tuple[int], spritesheet:SpriteSheet=None):
        super().__init__()
        self.gc = GameController()
        self.sheet = spritesheet

        self.size = np.array(size)
        self.speed = np.array(speed)
        self.color = np.array(color)

        self.screen = screen
        self._image = pg.Surface(size, pg.SRCALPHA)
        self._image.fill(self.color)

        self._rect = self._image.get_rect(center=np.array(init_center_pos))
        self.old_rect = self._rect.copy()

    @property
    def image(self):
        if self.sheet:
            self._image = self.sheet.get_image()
        else:
            self._image.fill(self.color)

        return self._image
    
    @property
    def rect(self):
        self._rect = self.image.get_rect(topleft=self._rect.topleft)
        return self._rect


    @property
    def dt(self):
        return self.gc.dt


    @property
    def screen_center(self):
        return np.array([
            self.screen.get_width(),
            self.screen.get_height()
        ]) / 2
    

    def update(self):
        super().update()

    def window_correction(self):
        if self._rect.top < 0:
            self._rect.top = 0
        elif self._rect.bottom > (h := self.screen.get_height()):
            self._rect.bottom = h

        if self._rect.left < 0:
            self._rect.left = 0
        elif self._rect.right > (w := self.screen.get_width()):
            self._rect.right = w

class PongPlayer(PongEntity):
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self._rect.y -= self.speed[1] * self.dt
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self._rect.y += self.speed[1] * self.dt

        self.window_correction()
        self.old_rect = self.rect.copy()


class PongBot(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, spritesheet:SpriteSheet=None):
        super().__init__(screen, size, init_center_pos, speed, color, spritesheet)

        self.ball:PongEntity = None

    def update(self): #todo logic using unimplemented methods
        if self.ball is None: return

        if self.ball_moving_towards_me():
            self.drift_towards(self.ball.rect.center)
        else:
            self.drift_towards(self.screen_center)

        self.window_correction()
        self.old_rect = self.rect.copy()


    def drift_towards(self, center:tuple):
        if self._rect.centery > center[1]:
            self._rect.y -= self.speed[1] * self.dt
        elif self._rect.centery < center[1]:
            self._rect.y += self.speed[1] * self.dt

    
    def ball_moving_towards_me(self) -> bool:
        ball_now = self.ball.rect.center
        ball_next = ball_now + self.ball.speed * self.dt

        dist_now = np.abs(self.rect.centerx - ball_now[0])
        dist_next = np.abs(self.rect.centerx - ball_next[0])

        return dist_next < dist_now
    

class PongBotAdvanced(PongBot):
    def __init__(self, screen, size, init_center_pos, speed, color, spritesheet = None):
        super().__init__(screen, size, init_center_pos, speed, color, spritesheet)

        self.cached_position = self.screen_center

    def update(self):
        if self.ball is None: return
        if self.ball_moving_towards_me():
            ball_half_width = self.ball._rect.width / 2
            paddle_axis = self._rect.right + ball_half_width if self.ball.speed[0] < 0 else self._rect.left - ball_half_width
            y = self.intersect(self.ball._rect.center, self.ball.speed, paddle_axis)
            y = self.bound(y, 0, self.screen.get_height())
            target = np.array([paddle_axis, y], dtype=int)

        else:
            target = self.screen_center

        if np.abs(target[1] - self.cached_position[1]) >= self._rect.height / 2:
            self.cached_position = target

        self.drift_towards(self.cached_position)
        self.window_correction()
        self.old_rect = self.rect.copy()


    def predict_ball_pos(self):
        pass #todo Optimize!

    @staticmethod
    def intersect(location:tuple[int], vector:tuple[int], axis_x) -> float:
        # x' = x + u1 * t -> t = (x' - x)/u1 (axis_x == x')
        # y' = y + u2 * t
        t = (axis_x - location[0])/vector[0]
        y = location[1] + vector[1]*t
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
    def __init__(self, screen, size, init_center_pos, speed, color, spritesheet:SpriteSheet=None):
        super().__init__(screen, size, init_center_pos, speed, color, spritesheet)

        self._image.fill((0, 0, 0, 0))
        pg.draw.ellipse(self._image, self.color, self._image.get_rect())

        self.g_bounce = pg.sprite.Group()

    @property
    def image(self):
        if self.sheet:
            self._image = self.sheet.get_image()
        else:
            pg.draw.ellipse(self._image, self.color, self._image.get_rect())

        return self._image

    def update(self):
        self._rect.x += self.speed[0] * self.dt
        self.speed *= self.handle_collisions(MovingDirection.Horizontal)

        self._rect.y += self.speed[1] * self.dt
        self.speed *= self.handle_collisions(MovingDirection.Vertical)

        self.window_correction()
        self.old_rect = self._rect.copy()

    def window_correction(self):
        super().window_correction()

        if self._rect.top <= 0 or self._rect.bottom >= self.screen.get_height():
            self.speed[1] *= -1

        if self._rect.left <= 0 or self._rect.right >= self.screen.get_width():
            self.speed[0] *= -1
            self._rect.center = self.screen_center

            self.color = np.array([255, 255, 255])
            #todo Score

    def handle_collisions(self, direction:MovingDirection) -> np.ndarray:
        if o := self._rect.collideobjects(list(self.g_bounce)):
            o:PongEntity

            self.color = o.color

            match direction:
                case MovingDirection.Horizontal:
                    if self._rect.left <= o._rect.right and self.old_rect.left >= o._rect.right:
                        self._rect.left = o._rect.right
                        return np.array([-1, 1])
                    
                    if self._rect.right >= o._rect.left and self.old_rect.right <= o._rect.left:
                        self._rect.right = o._rect.left
                        return np.array([-1, 1])

                case MovingDirection.Vertical:
                    if self._rect.top <= o._rect.bottom and self.old_rect.top >= o._rect.bottom:
                        self._rect.top = o._rect.bottom
                        return np.array([1, -1])
                    
                    if self._rect.bottom >= o._rect.top and self.old_rect.bottom <= o._rect.top:
                        self._rect.bottom = o._rect.top
                        return np.array([1, -1])
                    
        return np.array([1, 1])



