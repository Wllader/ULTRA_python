import pygame as pg, numpy as np
from enum import Enum, auto
from typing import Callable

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

class ClickState(Enum):
    RELEASED = auto()
    CLICKED = auto()
    HELD = auto()
    MISSED = auto()


class Widget(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, pos:np.ndarray, size:np.ndarray):
        super().__init__()

        self.mouse_held = np.zeros(3, dtype=bool)
        ...


class Button(Widget):
    pass

class Entry(Widget):
    pass