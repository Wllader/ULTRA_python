import pygame as pg, numpy as np
from enum import Enum, auto
from typing import Callable
from game_controller import GameController

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
        self.gc = GameController()

        self.screen = screen
        self._rect = pg.FRect(*pos, *size)
        self._image = pg.Surface(size, pg.SRCALPHA)

        self.mouse_held = np.zeros(3, dtype=bool)
        self._endabled = True

    def update(self, event:pg.Event=None):
        super().update()

    @property
    def dt(self):
        return self.gc.dt
    
    @property
    def rect(self):
        return self._rect
    
    @property
    def image(self):
        return self._image
    
    @property
    def enabled(self):
        return self._endabled
    
    @enabled.setter
    def enabled(self, value):
        self._endabled = value
    
    @property
    def size(self):
        return np.array(self._rect.size)
    
    @property
    def position(self):
        return np.array(self._rect.topleft)
    
    @property
    def center(self):
        return np.array(self._rect.center)
    
    def align_center(self, other:pg.Surface) -> np.ndarray:
        a = self.size
        b1 = other.size
        b2 = np.array(other.get_bounding_rect().size)
        b = (b1+b2)/2

        return np.abs(a-b)/2
    
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
        
        return ClickState.UNKNOWN
    
    def toggle(self):
        self.enabled = not self.enabled


class Label(Widget): ...

class Button(Widget): ...

class Entry(Widget): ...

#? Bonus:
class CheckBox(Widget): ...
class Canvas(Widget): ... #!
class BarPlot(Widget): ... #!