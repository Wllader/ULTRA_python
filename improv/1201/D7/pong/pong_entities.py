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
            self._image = self.sheet.get_image()
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

class PongBall(PongEntity): #todo Handle collisions (bouncing)
    def __init__(self, screen, size, init_center_pos, speed, color = (255, 255, 255), spritesheet:SpriteSheet=None):
        super().__init__(screen, size, init_center_pos, speed, color, spritesheet)

        self._image.fill((0, 0, 0, 0))
        pg.draw.ellipse(self._image, self.color, self._image.get_frect())

        self.g_bounce = pg.sprite.Group()

    @property
    def image(self):
        if self.sheet:
            self._image = self.sheet.get_image()
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

        if self.rect.left <= 0 or self.rect.right >= self.screen.width:
            self.speed[0] *= -1
            self.color = (255, 255, 255)
            self.rect.center = (
                self.screen_center[0],
                np.random.randint(0, self.screen.height)
            )
            #todo Score

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