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


class Plot(Widget):
    def __init__(self, screen, pos, size):
        super().__init__(screen, pos, size)