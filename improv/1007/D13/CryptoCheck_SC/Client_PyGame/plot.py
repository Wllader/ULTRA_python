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

        self._center_pos=np.array(self._rect.center)
        self._new_center_pos=self._center_pos.copy()

        self._rect = self._image.get_rect(center=self._center_pos)

        self.color_tween = Tween.EaseOutSine(1000, clipped=(0, 255))
        self.pos_tween = Tween.EaseOutSine(1000)

    @property
    def rect(self):
        self._rect = self._image.get_rect(center=self.position)

    @property
    def position(self):
        return self.pos_tween.tweenify(self._center_pos, self._new_center_pos)
    
    @position.setter
    def position(self, value):
        self._center_pos = self.position
        self._new_center_pos = np.array(value)
        self.pos_tween.reset()

    @property
    def image(self):
        self._image.fill(self.color)

    @property
    def color(self):
        return self.color_tween.tweenify(self._color, self._new_color)
    
    @color.setter
    def color(self, value):
        self._color = self.color
        self._new_color = np.array(value)
        self.color_tween.reset()

    

class Plot(Widget):
    def __init__(self, screen, pos, size):
        super().__init__(screen, pos, size)

        self._image = pg.Surface(size, pg.SRCALPHA)
        self.set_data(np.random.rand(50)*250)

        w=1
        h=3

        self.particles = pg.sprite.Group(*[
            Particle(self._image, (w*i, 0), (w, h)) for i in range(0, size[0], w)
        ])

        self.move_particles()

    @property
    def image(self):
        self._image.fill((0, 0, 0, 15))
        self.particles.draw(self._image)
        return self._image
    
    def set_data(self, data:np.ndarray, num_parts=50):
        num_parts = np.clip(num_parts, 2, self.size[0])
        I = np.linspace(0, len(data), num_parts, endpoint=False, dtype=int)
        self.data:np.ndarray = data[I] #! Not precise

    def move_particles(self):
        temp_data:np.ndarray = self.data.copy()

        temp_data -= temp_data.min()
        temp_data /= temp_data.max()
        temp_data = temp_data.clip(0, 1)

        I = np.arange(len(self.particles)) / (len(self.particles) - 1) * (len(temp_data) - 1)
        I = I.round().astype(int)

        random_colors = np.random.randint(0, 256, (2, 3))
        particles:list[Particle] = list(self.particles)
        for i in range(len(particles)):
            x, _ = particles[i]._center_pos
            t = temp_data[I[i]]

            particles[i].position = (x, (1-t)*self.size[1])
            particles[i].color = ((1-t)*random_colors[0] + t*random_colors[1])
