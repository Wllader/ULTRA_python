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

class HoverState(Enum):
    CAME_IN = auto()
    IN = auto()
    CAME_OUT = auto()
    OUT = auto()
    UNKNOWN = auto()

class Widget(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, pos:tuple[int], size:tuple[int]):
        super().__init__()
        self.gc = GameController()

        self.screen = screen
        self._rect = pg.FRect(*pos, *size)
        self._image = pg.Surface(size, pg.SRCALPHA)

        self.mouse_held = np.zeros(3, dtype=bool)
        self.is_hovered = False

        self._endabled = True
        self.dirty = False

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
    
    def hover(self) -> HoverState:
        c = self._rect.collidepoint(pg.mouse.get_pos())
        h = self.is_hovered

        if c and not h:
            self.is_hovered = True
            return HoverState.CAME_IN
        elif c and h:
            return HoverState.IN
        elif not c and h:
            self.is_hovered = False
            return HoverState.CAME_OUT
        elif not c and not h:
            return HoverState.OUT
        
        return HoverState.UNKNOWN
    
    def click(self, button:int) -> ClickState:
        p = pg.mouse.get_pressed()[button]
        h = self.mouse_held[button]
        c = self.hover() == HoverState.IN

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


class Label(Widget):
    def __init__(self, screen, pos, size, text:str, font=None, fg:tuple[int]=WHITE, bg:tuple[int]=NONE):
        super().__init__(screen, pos, size)

        self.text = text
        self.font = font or pg.font.SysFont("Calibri", int(self.size[1] // 2))
        self.fg = fg
        self.bg = bg

        self.dirty = True

    @property
    def image(self):
        if self.dirty:
            label = self.font.render(self.text, True, self.fg, None if (self.bg == NONE).all() else self.bg) #!
            pos = self.align_center(label)
            self._image.blit(label, pos)
            self.dirty = False

        return self._image

class Button(Widget):
    def __init__(self, screen, pos, size, text:str, font=None, fg:tuple[int]=BLACK, bg:tuple[int]=WHITE, command:Callable=lambda: print("Clicked!")):
        super().__init__(screen, pos, size)

        self.text = text
        self.font = font or pg.font.SysFont("Calibri", int(self.size[1] // 2))
        self.fg = fg
        self.bg = bg
        self.command = command

        self.dirty = True

    @property
    def image(self):
        if self.dirty:
            self._image.fill(self.bg)
            label = self.font.render(self.text, True, self.fg)
            pos = self.align_center(label)
            self._image.blit(label, pos)

            if self.mouse_held[0]: #!
                self._image.fill(GREY * 150, special_flags=pg.BLEND_RGBA_MULT)

            elif self.is_hovered:
                self._image.fill(GREY * 200, special_flags=pg.BLEND_RGBA_MULT)

            self.dirty = False

        return self._image
    
    def update(self, event=None):
        super().update(event)

        if self.hover() in (HoverState.CAME_IN, HoverState.CAME_OUT):
            self.dirty = True

        if (s := self.click(0)) in (ClickState.CLICKED, ClickState.RELEASED):
            if s == ClickState.CLICKED:
                self.command()

            self.dirty = True
    

class Entry(Widget):
    def __init__(self, screen, pos, size, font=None, fg:tuple[int]=WHITE, bg:tuple[int]=GREY*28, default_text:str="", placeholder_text:str=""):
        super().__init__(screen, pos, size)

        self.font = font or pg.font.SysFont("Calibri", int(self.size[1] // 2))
        self.fg = fg
        self.bg = bg
        self.text = default_text
        self.placeholder = placeholder_text

        self.selected = False
        self.dirty = True

    @property
    def has_text(self) -> bool:
        return self.text != ""

    @property
    def image(self):
        if self.dirty:
            self._image.fill(self.bg)
            if self.has_text:
                label = self.font.render(self.text, True, self.fg)
            else:
                label = self.font.render(self.placeholder, True, self.fg * .6)

            pos = self.align_center(label)
            self._image.blit(label, pos)

            if self.selected:
                self._image.fill(GREY * 60, special_flags=pg.BLEND_RGBA_ADD)
            if self.hover() == HoverState.IN:
                self._image.fill(GREY * 200, special_flags=pg.BLEND_RGBA_MULT)

            self.dirty = False

        return self._image
    
    def update(self, event=None):
        super().update(event)

        if self.hover() in (HoverState.CAME_IN, HoverState.CAME_OUT):
            self.dirty = True

        match self.click(0):
            case ClickState.CLICKED:
                self.selected = True
                self.dirty = True
            case ClickState.MISSED:
                self.selected = False
                self.dirty = True

        if self.selected and event and event.type == pg.KEYDOWN:
            match event.key:
                case pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                case pg.K_RETURN:
                    self.selected = False
                case _:
                    self.text += event.unicode

            self.dirty = True

            

#? Bonus:
class CheckBox(Widget): ...
class Canvas(Widget): ... #!
class BarPlot(Widget): ... #!