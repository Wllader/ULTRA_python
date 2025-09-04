import pygame as pg
import numpy as np
from widgets import Widget
from tween import Tween

GREY = np.ones(3)
WHITE = GREY * 255
BLACK = np.zeros(3)
RED = np.array((255, 0, 0))
BLUE = np.array((0, 0, 255))

class Particle(Widget):
    def __init__(self, screen, pos, size, color=BLUE):
        super().__init__(screen, pos, size)

        self._color = color
        self._new_color = self._color.copy()
        self._image.fill(self._color)

        self._center_pos = np.array(self._rect.center)
        self._new_center_pos = self._center_pos.copy()

        self._rect = self._image.get_rect(center=self._center_pos)

        self.pos_tween = Tween.EaseInOutCubic(np.random.randint(500, 1500, 1))
        self.color_tween = Tween.EaseInOutCubic(np.random.randint(500, 1500, 1))

    @property
    def position(self):
        if (self._center_pos != self._new_center_pos).any():
            p, s = self.pos_tween.get_state(self._center_pos, self._new_center_pos)
            if s:
                self._center_pos = self._new_center_pos
                return self._new_center_pos
            return p
        return self._center_pos

    @property
    def rect(self):
        self._rect = self._image.get_rect(center=self.position)
        return self._rect #new Tohle je potřeba vrátit!

    @property
    def color(self):
        if (self._color != self._new_color).any():
            c, s = self.color_tween.get_state(self._color, self._new_color)
            if s:
                self._color = self._new_color
                return self._new_color
            return c
        return self._color
    
    @property
    def image(self):
        self._image.fill(self.color)
        return self._image
    

    def change_position(self, pos):
        self._new_center_pos = np.array(pos)
        self.pos_tween.reset()

    def change_color(self, color):
        self._new_color = np.array(color)
        self.color_tween.reset()



class Plot(Widget):
    def __init__(self, screen, pos, size):
        super().__init__(screen, pos, size)

        self.set_data(np.random.rand(50) * 250)

        w = 1
        self.particles = pg.sprite.Group(*[
            Particle(self._image, np.array([w*i, 0]), np.array([w, 3])) for i in range(size[0])
        ])

        self.move_particles()

    def set_data(self, data, num_parts=50):
        num_parts = np.clip(num_parts, 2, self.size[0])
        I = np.linspace(0, len(data), num_parts, endpoint=False, dtype=int)
        self.data:np.ndarray = data[I] #! Not precise

    def move_particles(self):
        temp_data:np.ndarray = self.data.copy()

        temp_data -= temp_data.min()
        temp_data /= temp_data.max()
        temp_data.clip(0, 1)

        I = np.arange(len(self.particles)) / (len(self.particles)-1) * (len(temp_data) - 1)
        I = I.round().astype(int)

        for i in range(len(self.particles)):
            particles:list[Particle] = list(self.particles)
            x, _ = particles[i]._center_pos
            t = temp_data[I[i]]
            particles[i].change_position((x, (1-t) * self.size[1]))
            particles[i].change_color((1-t)*BLUE + t*RED)

    @property
    def image(self):
        self._image.fill(BLACK)
        self.particles.draw(self._image)

        return self._image
