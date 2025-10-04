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
    def pozision(self):
        return np.array(self._rect.topleft)
    
    @property
    def center(self):
        return np.array(self._rect.center)
    
    @staticmethod
    def align_center(a:tuple, b:tuple):
        a = np.array(a)
        b = np.array(b)
        return np.abs(a-b)//2
    
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
        
    def hover(self) -> bool:
        return self._rect.collidepoint(pg.mouse.get_pos())



class Button(Widget):
    def __init__(self, screen, pos, size, text:str, font=None, fg:tuple[int] = BLACK, bg:tuple[int] = WHITE, command=lambda: print("Clicked!")):
        super().__init__(screen, pos, size)
        
        self.text = text
        self.font:pg.font.Font = font if font is not None else pg.font.SysFont("Calibri", self.size[1]//2)
        self.fg = fg
        self.bg = bg
        self.command = command

    @property
    def image(self):
        self._image.fill(self.bg)
        label = self.font.render(self.text, True, self.fg)
        pos = self.align_center(self.size, label.get_rect().size)
        self._image.blit(label, pos)

        if self.mouse_held[0]:
            self._image.fill(GREY * 150, special_flags=pg.BLEND_RGBA_MULT)
        elif self.hover():
            self._image.fill(GREY * 200, special_flags=pg.BLEND_RGBA_MULT)

        return self._image
    
    def update(self, event=None):
        super().update(event)

        if self.click(0) == ClickState.CLICKED:
            self.command()


class Entry(Widget):
    def __init__(self, screen, pos, size, font=None, fg:tuple[int] = WHITE, bg:tuple[int] = GREY*28, default_text:str="", tooltip_text:str=""):
        super().__init__(screen, pos, size)
        
        self.font = font if font is not None else pg.font.SysFont("Calibri", self.size[1]//2)
        self.fg = fg
        self.bg = bg
        self.text = default_text
        self.tooltip = tooltip_text

        self.selected = False

    @property
    def image(self):
        self._image.fill(self.bg)
        if self.has_text():
            label = self.font.render(self.text, True, self.fg)
        else:
            label = self.font.render(self.tooltip, True, self.fg * .6)

        pos = self.align_center(self.size, label.get_rect().size)
        self._image.blit(label, pos)

        if self.selected:
            self._image.fill(GREY * 60, special_flags=pg.BLEND_RGBA_ADD)
        if self.hover():
            self._image.fill(GREY * 200, special_flags=pg.BLEND_RGBA_MULT)

        return self._image

    def has_text(self) -> bool:
        return self.text != ""
    
    def update(self, event:pg.event.Event=None):
        super().update(event)

        match self.click(0):
            case ClickState.CLICKED:
                self.selected = True
            case ClickState.MISSED:
                self.selected = False

        if self.selected and event and event.type == pg.KEYDOWN:
            match event.key:
                case pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                case pg.K_RETURN:
                    self.selected = False
                case _:
                    self.text += event.unicode
    