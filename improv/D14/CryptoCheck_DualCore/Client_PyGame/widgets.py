import pygame as pg
import numpy as np
from enum import Enum, auto

class ClickState(Enum):
    RELEASED = auto()
    CLICKED = auto()
    HELD = auto()
    MISSED = auto()

GREY = np.ones(3)
WHITE = GREY * 255
BLACK = np.zeros(3)

class Widget(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, pos:np.ndarray, size:np.ndarray):
        super().__init__()

        self.screen = screen
        self._rect = pg.Rect(*pos, *size)
        self._image = pg.Surface(size)

        self.mouse_held = np.zeros(3, dtype=bool)

    def update(self, event=None):
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
        return np.array((
            self._rect.x,
            self._rect.y
        ))
    
    @property
    def center(self):
        return np.array(self._rect.center)
    

    @staticmethod
    def align_center(s1:tuple, s2:tuple):
        return np.abs(np.array(s1) - np.array(s2)) // 2
    
    def click(self, button:int) -> ClickState:
        p = pg.mouse.get_pressed()[button]
        h = self.mouse_held[button]
        c = self._rect.collidepoint(pg.mouse.get_pos())

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
    def __init__(self, screen, pos, size, text:str, font=None, fg:np.ndarray=BLACK, bg:np.ndarray=WHITE, command=lambda: print("Clicked!")):
        super().__init__(screen, pos, size)

        self.text:str = text
        self.font:pg.font.Font = font if font is not None else pg.font.SysFont("Calibri", self.size[1] // 2)
        self.bg = bg
        self.fg = fg
        self.command = command
        
        self.mouse_held = np.zeros(3, dtype=bool)

    @property
    def image(self):
        self._image.fill(self.bg)
        label = self.font.render(self.text, True, self.fg)
        pos = self.align_center(self.size, label.get_rect().size)
        self._image.blit(label, pos)

        return self._image

    def update(self, event=None):
        if self.click(0) == ClickState.CLICKED:
            self.command()


class Entry(Widget):
    def __init__(self, screen, pos, size, font=None, fg:np.ndarray=WHITE, bg:np.ndarray=GREY * 28, default_text=""):
        super().__init__(screen, pos, size)

        self.font = font if font is not None else pg.font.SysFont("Calibri", self.size[1] // 2)
        self.fg = fg
        self.bg = bg
        self.text = default_text

        self.mouse_held = np.zeros(3, dtype=bool)
        self.selected = False

    @property
    def image(self):
        self._image.fill(self.bg if not self.selected else GREY*95)
        label = self.font.render(self.text, True, self.fg)
        pos = self.align_center(self.size, label.get_rect().size)
        self._image.blit(label, pos)

        return self._image

    def update(self, event:pg.event.Event=None):
        if self.click(0) == ClickState.CLICKED:
            self.selected = True
        
        if self.click(0) == ClickState.MISSED:
            self.selected = False

        if self.selected and event and event.type == pg.KEYDOWN:
            match event.key:
                case pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                case pg.K_RETURN:
                    self.selected = False
                case _:
                    self.text += event.unicode

    
