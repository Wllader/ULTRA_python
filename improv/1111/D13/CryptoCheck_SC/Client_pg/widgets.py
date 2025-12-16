import pygame as pg, numpy as np
from enum import Enum, auto
from typing import Callable

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0
NONE = np.zeros(4, dtype=np.uint8)

class ClickState(Enum):
    CLICKED = auto()
    HELD = auto()
    RELEASED = auto()
    MISSED = auto()
    UNKNOWN = auto()

class Widget(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, pos:tuple[int], size:tuple[int]):
        super().__init__()
        ...

class Label(Widget):
    def __init__(self, screen, pos, size, text:str, font=None, fg:tuple[int]=WHITE, bg:tuple[int]=NONE):
        super().__init__(screen, pos, size)

        self.text = text
        self.font:pg.font.Font = font if font is not None else pg.font.SysFont("Calibri", self.size[1] // 2)
        ...

class Button(Widget):
    def __init__(self, screen, pos, size, text:str, font=None, fg:tuple[int]=BLACK, bg:tuple[int]=WHITE, command=lambda:print("Clicked!")):
        super().__init__(screen, pos, size)

class Entry(Widget):
    def __init__(self, screen, pos, size, font=None, fg:tuple[int]=WHITE, bg:tuple[int]=GREY*28, default_text:str="", placeholder_text:str=""):
        super().__init__(screen, pos, size)
        ...



#? Bonus:
class CheckBox(Widget):
    pass

class Canvas(Widget):
    pass

class BarPlot(Widget):
    pass