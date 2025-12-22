import pygame as pg, numpy as np
from game_controller import GameController
from enum import Enum, auto

class ClickState(Enum):
    CLICKED = auto()
    HELD = auto()
    RELEASED = auto()
    MISSED = auto()
    UNKNOWN = auto()

class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, init_center_pos:tuple[int]):
        super().__init__()

        self.gc = GameController()
        self.screen = screen
        self._image = pg.Surface((50, 50), pg.SRCALPHA)
        self._rect = self._image.get_frect(center=init_center_pos)

        self.mk_held = np.zeros(3, dtype=bool)

    @property
    def rect(self):
        return self._rect
    
    @property
    def image(self):
        return self._image
    
    def click(self, button:int) -> ClickState:
        p = pg.mouse.get_pressed()[button]
        h = self.mk_held[button]
        c = self.rect.collidepoint(pg.mouse.get_pos())

        if p and not h and c:
            self.mk_held[button] = True
            return ClickState.CLICKED
        
        elif p and h and c:
            return ClickState.HELD
        
        elif not p and h:
            return ClickState.RELEASED
        
        elif p and not h and not c:
            return ClickState.MISSED
        
        return ClickState.UNKNOWN
    
class Square(Entity):
    def __init__(self, screen, init_center_pos):
        super().__init__(screen, init_center_pos)

        