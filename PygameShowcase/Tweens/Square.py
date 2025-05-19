import pygame as pg, numpy as np
from GameController import GameController
from Tweens import Tweens

class Square(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, init_center_pos:np.ndarray, *groups, speed:float = None):
        self.screen = screen
        self.screen_size = np.array(self.screen.get_size())

        self._color_old = np.array([0, 0, 0])
        self._color_new = np.random.randint(0, 256, 3)
        self.mid_trans = True

        self.speed = np.abs(np.random.randn(1)) + 1 if speed is None else speed

        self.tween = Tweens(1000)
        self._image = pg.Surface((50, 50))
        self._image.fill(self.color)
        self.rect = self._image.get_rect(center=init_center_pos)

        self.gc = GameController()
        self.mouse_held = [False, False, False]

        super().__init__(*groups)

    @property
    def image(self):
        self._image.fill(self.color)
        return self._image

    @property
    def color(self):
        if (self._color_old != self._color_new).all():
            clr, state = self.tween.get_state(self._color_old, self._color_new)
            if state:
                self._color_old = self._color_new

            return clr
        else:
            return self._color_old


    def update(self):
        self.rect.centery += self.speed * self.gc.dt

        if self.rect.top > self.screen_size[1] + 10:
            self.kill()

        if self.click(2):
            self._color_new = np.random.randint(0, 256, 3)
            self.tween.reset()


    def click(self, button:int) -> bool:
        if (p := pg.mouse.get_pressed()[button]) and not self.mouse_held[button] and self.rect.collidepoint(pg.mouse.get_pos()):
            self.mouse_held[button] = True
            return True
        elif not p:
            self.mouse_held[button] = False
            return False