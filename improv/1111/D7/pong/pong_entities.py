import pygame as pg, numpy as np

#Todo vytvořit základní PongEntity
#Todo Odvodit od ní PongPlayer, PongBot a PongBall objekty a implementovat jejich základní chování


class PongEntity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, size:tuple[int], init_center_pos:tuple[int], speed:tuple[int], color:tuple[int]):
        super().__init__()

        self.size = np.array(size)
        self.speed = np.array(speed)
        self.color = np.array(color)

        self.screen = screen
        self._image = pg.Surface(size, pg.SRCALPHA)
        self._image.fill(self.color)

        self.rect = self._image.get_rect(center=np.array(init_center_pos))
        self.old_rect = self.rect.copy()

    @property
    def image(self):
        return self._image
    

    @property
    def screen_center(self):
        return np.array([
            self.screen.get_width(),
            self.screen.get_height()
        ]) / 2
    

    def update(self, dt):
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
    def update(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.rect.y -= self.speed[1] * dt
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.rect.y += self.speed[1] * dt

        self.window_correction()
        self.old_rect = self.rect.copy()


class PongBot(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color):
        super().__init__(screen, size, init_center_pos, speed, color)

        self.ball:PongEntity = None

    def update(self, dt): #todo logic using unimplemented methods
        if self.ball:
            self.rect.centery = self.ball.rect.centery

        self.window_correction()

    def drift_towards(self, center:tuple): #todo Implement drifiting towards given coordinates (with our speed)
        pass

    
    def ball_moving_towards_me(self) -> bool: #todo Implement
        pass


class PongBall(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color):
        super().__init__(screen, size, init_center_pos, speed, color)

        self._image.fill((0, 0, 0, 0))
        pg.draw.ellipse(self._image, self.color, self._image.get_rect())

        self.g_bounce = pg.sprite.Group()

    def update(self, dt):
        self.rect.x += self.speed[0] * dt
        self.rect.y += self.speed[1] * dt

        self.window_correction()
        self.old_rect = self.rect.copy()

    def window_correction(self):
        super().window_correction()

        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height():
            self.speed[1] *= -1

        if self.rect.left <= 0 or self.rect.right >= self.screen.get_width():
            self.speed[0] *= -1
            self.rect.center = self.screen_center
            #todo Score


