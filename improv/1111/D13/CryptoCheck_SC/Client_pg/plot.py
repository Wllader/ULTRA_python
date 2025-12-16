import pygame as pg, numpy as np
from widgets import Widget
from tween import Tween

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0
BLUE = np.array((0, 0, 255), dtype=np.uint8)


class Particle(Widget):
    def __init__(self, screen, pos, size, color:np.ndarray=BLUE):
        super().__init__(screen, pos, size)

        self._color = color
        self._new_color = self._color.copy()
        self._image.fill(self._color)

        self._center_pos = np.array(self._rect.center)
        self._new_center_pos = self._center_pos.copy()

        self.color_tween = Tween.EaseInOutExpo(1000, clipped=(0, 255))
        self.pos_tween = Tween.EaseOutSine(1000)

    @property
    def rect(self):
        self._rect = self._image.get_frect(center=self.position)
        return self._rect

    @property
    def position(self): pass

    @position.setter
    def position(self, value): pass

    @property
    def image(self):
        self._image.fill(self.color)
        return self._image
    
    @property
    def color(self): pass

    @color.setter
    def color(self, value): pass


class Plot(Widget):
    def __init__(self, screen, pos, size):
        super().__init__(screen, pos, size)

        ...

    def set_data(self, data:np.ndarray, num_parts=50): pass

    def move_particles(self): pass