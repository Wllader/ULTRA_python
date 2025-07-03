import pygame as pg, numpy as np
from widgets import Widget
from tween import Tween

GREY = np.ones(3)
WHITE = GREY * 255
BLACK = np.zeros(3)
RED = np.array((255, 0, 0))
BLUE = np.array((0, 0, 255))

class Particle(Widget):
    pass

class Plot(Widget):
    pass