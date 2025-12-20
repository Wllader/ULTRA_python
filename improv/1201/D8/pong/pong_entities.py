import pygame as pg, numpy as np
from enum import Enum, auto
from game_controller import GameController
from spritesheet_sr_fc import SpriteSheet

#Todo Vytvořit základní PongEntity
#Todo odvodit od ní PongPlayer, PongBot a PongBall objekty
#Todo implementovat základní chování objektů

class MovingDirection(Enum):
    Horizontal = auto()
    Vertical = auto()


class PongEntity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, size:tuple[int], init_center_pos:tuple[int], speed:tuple[int], color:tuple[int] = (255, 255, 255), spritesheet:SpriteSheet=None):
        super().__init__()
        self.gc = GameController()
        self.sheet = spritesheet

        self.size = np.array(size)
        self.speed = np.array(speed)
        self.color = np.array(color)

        self.screen = screen
        self._image = pg.Surface(size, pg.SRCALPHA)
        self._image.fill(self.color)

        self.rect = self._image.get_frect(center=init_center_pos)
        self.old_rect = self.rect.copy()

    @property
    def image(self):
        if self.sheet:
            self._image = self.sheet.frame
            self.rect = self._image.get_frect(center=self.rect.center)
        return self._image

    @property
    def dt(self):
        return self.gc.dt

    @property
    def screen_center(self):
        return np.array([
            self.screen.width,
            self.screen.height
        ]) / 2
    
    def update(self):
        super().update()

    def window_correction(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > (h := self.screen.height):
            self.rect.bottom = h

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > (w := self.screen.width):
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
    def __init__(self, screen, size, init_center_pos, speed, color = (255, 255, 255), spritesheet:SpriteSheet=None):
        super().__init__(screen, size, init_center_pos, speed, color, spritesheet)

        self.ball:PongEntity = None

    def update(self):
        if self.ball is None: return

        if self.ball_moving_towards_me():
            self.drift_towards(self.ball.rect.center)
        else:
            self.drift_towards(self.screen_center)

        self.window_correction()
        self.old_rect = self.rect.copy()

    def drift_towards(self, center:tuple):
        if self.rect.centery > center[1]:
            self.rect.y -= self.speed[1] * self.dt
        elif self.rect.centery < center[1]:
            self.rect.y += self.speed[1] * self.dt

    def ball_moving_towards_me(self) -> bool:
        if not self.ball: return False
        ball_now = self.ball.rect.center
        ball_next = ball_now + self.ball.speed * self.dt

        dist_now = np.abs(self.rect.centerx - ball_now[0])
        dist_next = np.abs(self.rect.centerx - ball_next[0])

        return dist_next < dist_now
    
class PongBotAdvanced(PongBot):
    def __init__(self, screen, size, init_center_pos, speed, color=(255, 255, 255), spritesheet = None):
        super().__init__(screen, size, init_center_pos, speed, color, spritesheet)

        self.chached_pos = self.screen_center

    def update(self):
        if self.ball is None: return
        if self.ball_moving_towards_me():
            y = self.predict_ball_pos()
            target = (0, int(y))

        else:
            target = self.screen_center

        if np.abs(target[1] - self.chached_pos[1]) >= self.rect.height / 2:
            self.chached_pos = target

        self.drift_towards(self.chached_pos)
        self.window_correction()
        self.old_rect = self.rect.copy()

    def predict_ball_pos(self) -> float:
        ball_half_width = self.ball.rect.width / 2
        paddle_axis = self.rect.right + ball_half_width if self.ball.speed[0] < 0 else self.rect.left - ball_half_width
        y = self.intersect(self.ball.rect.center, self.ball.speed, paddle_axis)
        y = self.bound(y, 0, self.screen.height)
        return y

    @staticmethod
    def intersect(location:tuple[int], vector:tuple[int], x_hat) -> float:
        # (u1, u2) = vector, (x, y) = location
        # x' = x + u1 * t -> t = (x_hat - x)/u1
        # y' = y + u2 * t
        t = (x_hat - location[0])/vector[0]
        y = location[1] + vector[1] * t
        return y

    @staticmethod
    def intersect_implicit_func(location:tuple[int], vector:tuple[int], x_hat) -> float:
        # ax + by + c = 0
        # c -> -(ax + by): (-b, a) = vector, (x, y) = location
        # y' = (ax_hat + c)/(-b)
        normal = np.array(vector[::-1])
        normal[0] *= -1

        c = -np.dot(normal, location)
        y = (normal[0] * x_hat + c)/(-normal[1])
        return y

    @staticmethod
    def bound(y:float, lower_bound:int, upper_bound:int) -> float:
        #neefektivní bound
        if y >= lower_bound and y <= upper_bound:
            return y
        
        if y < lower_bound:
            y0 = np.abs(lower_bound - y)
            return PongBotAdvanced.bound(y + 2*y0, lower_bound, upper_bound)
        
        if y > upper_bound:
            y0 = np.abs(upper_bound - y)
            return PongBotAdvanced.bound(y - 2*y0, lower_bound, upper_bound)

    @staticmethod
    def bound(y:float, lower_bound:int, upper_bound:int) -> float:
        span = upper_bound - lower_bound

        pos = (y - lower_bound) % (2*span)
        if pos > span:
            pos = 2*span - pos

        return pos + lower_bound

class PongBall(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color = (255, 255, 255), spritesheet:SpriteSheet=None):
        super().__init__(screen, size, init_center_pos, speed, color, spritesheet)

        self._image.fill((0, 0, 0, 0))
        pg.draw.ellipse(self._image, self.color, self._image.get_frect())

        self.g_bounce = pg.sprite.Group()

    @property
    def image(self):
        if self.sheet:
            self._image = self.sheet.frame
        else:
            self._image.fill((0, 0, 0, 0))
            pg.draw.ellipse(self._image, self.color, self._image.get_frect())
        return self._image

    def update(self):
        self.rect.x += self.speed[0] * self.dt
        self.speed *= self.handle_collisions(MovingDirection.Horizontal)

        self.rect.y += self.speed[1] * self.dt
        self.speed *= self.handle_collisions(MovingDirection.Vertical)

        self.window_correction()
        self.old_rect = self.rect.copy()

    def window_correction(self):
        super().window_correction()

        if self.rect.top <= 0 or self.rect.bottom >= self.screen.height:
            self.speed[1] *= -1

        if (l := self.rect.left <= 0) or self.rect.right >= self.screen.width:
            self.speed[0] *= -1
            self.color = (255, 255, 255)
            self.rect.center = (
                self.screen_center[0],
                np.random.randint(0, self.screen.height)
            )

            # self.gc.score(1) if l else self.gc.score(0)
            self.gc.score(int(l))
            
    def ccd(start:tuple[int], end:tuple[int], known:float, axis:int) -> tuple[np.ndarray, float]:
        # a := start, b := end
        # (1-t)*a + t*b = known
        # (1-t)*a_y + t*b_y = known_y
        # -> t = (known-a)/(b-a)
        ...

    def bounce(self, known:float, axis:int):
        # Change direction based on CCD
        ...

    def handle_collisions(self, direction:MovingDirection) -> np.ndarray:
        if o := self.rect.collideobjects(list(self.g_bounce)):
            o:PongEntity
            self.color = o.color

            match direction:
                case MovingDirection.Horizontal:
                    dx = self.rect.x - self.old_rect.x

                    if dx > 0: #Rigth
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