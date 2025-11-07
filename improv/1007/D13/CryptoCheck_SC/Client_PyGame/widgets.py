import pygame as pg, numpy as np
from enum import Enum, auto
from typing import Callable

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

class ClickState(Enum):
    CLICKED = auto()
    HELD = auto()
    RELEASED = auto()
    MISSED = auto()

class Widget(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, pos:tuple[int], size:tuple[int]):
        super().__init__()

        self.screen = screen
        self._rect = pg.Rect(*pos, *size)
        self._image = pg.Surface(size)

        self.mouse_held = np.zeros(3, dtype=bool)

    def update(self, event:pg.event.Event=None):
        super().update()

    @property
    def rect(self):
        return self._rect
    
    @property
    def image(self):
        return self._image
    
    @property
    def size(self):
        return np.array(self._rect.size)
    
    @property
    def position(self):
        return np.array(self._rect.topleft)
    
    @property
    def center(self):
        return np.array(self._rect.center)
    
    @staticmethod
    def align_center(a:tuple, b:tuple):
        a_ = np.array()
        b_ = np.array()
        return np.abs(a_-b_)//2
    
    def hover(self) -> bool:
        return self._rect.collidepoint(pg.mouse.get_pos())

    def click(self, button:int) -> ClickState:
        p = pg.mouse.get_pressed()[button]
        h = self.mouse_held[button]
        c = self.hover()

        if p and not h and c:
            self.mouse_held[button] = True
            return ClickState.CLICKED
        elif p and h and c:
            return ClickState.HELD
        elif not p and h:
            self.mouse_held[button] = False
            return ClickState.RELEASED
        elif p and not h and not c:
            return ClickState.MISSED
        
    
class Button(Widget):
    def __init__(self, screen, pos, size, text:str, font=None, fg:tuple[int] = BLACK, bg:tuple[int] = WHITE, command:Callable=lambda: print("Clicked!")):
        super().__init__(screen, pos, size)


class Entry(Widget):
    def __init__(self, screen, pos, size, font=None, fg:tuple[int] = WHITE, bg:tuple[int] = GREY*28, default_text:str="", tooltip_text:str=""):
        super().__init__(screen, pos, size)

