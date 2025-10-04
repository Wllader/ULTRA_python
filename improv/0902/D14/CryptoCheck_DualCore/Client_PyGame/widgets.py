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
    def __init__(self, screen:pg.Surface, pos:tuple[int], size:tuple[int]):
        super().__init__()
        ...


class Button(Widget):
    def __init__(self, screen, pos, size, text:str, font=None, fg:tuple[int] = BLACK, bg:tuple[int] = WHITE, command=lambda: print("Clicked!")):
        super().__init__(screen, pos, size)
        ...


class Entry(Widget):
    def __init__(self, screen, pos, size, font=None, fg:tuple[int] = BLACK, bg:tuple[int] = WHITE, default_text:str="", tooltip_text:str=""):
        super().__init__(screen, pos, size)
        ...