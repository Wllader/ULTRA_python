import pygame as pg, numpy as np
from game_controller import GameController
from enum import Enum, auto
from tween import Tween

class ClickState(Enum):
    CLICKED = auto()
    HELD = auto()
    RELEASED = auto()
    MISSED = auto()



class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, init_center_pos:tuple[int]):
        super().__init__()

        self.gc = GameController()

        self.screen = screen
        self._image = pg.Surface((50, 50))
        self._rect = self._image.get_rect(center=init_center_pos)

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
            self.mk_held[button] = False
            return ClickState.RELEASED
        elif p and not h and not c:
            return ClickState.MISSED
    

class Square(Entity):
    def __init__(self, screen, init_center_pos):
        super().__init__(screen, init_center_pos)

        self._color = np.random.randint(0, 256, 3)
        self._new_color = self._color.copy()
        
        self._center_pos = np.array(init_center_pos)
        self._new_center_pos = self._center_pos.copy()

        self._image.fill(self._color)

        self.color_tween = Tween(1000, clipped=True)
        self.pos_tween = Tween.EaseOutQuint(1000)


    @property
    def image(self):
        self._image.fill(self.color)
        return self._image
    
    @property
    def color(self):
        if self.color_tween is None:
            self._color = self._new_color
            return self._color
        
        return self.color_tween.tweenify(self._color, self._new_color)
    

    @property
    def rect(self):
        self._rect = self._image.get_rect(center=self.center_pos)
        return self._rect
    
    @property
    def center_pos(self):
        if self.pos_tween is None:
            self._center_pos = self._new_center_pos
            return self._center_pos
        
        return self.pos_tween.tweenify(self._center_pos, self._new_center_pos)


    def update(self):
        if self.click(1) == ClickState.CLICKED:
            self.kill()

        if self.click(2) == ClickState.CLICKED:
            self.change_color(np.random.randint(0, 256, 3))


        if self.click(2) == ClickState.RELEASED:
            self.change_position(np.array(pg.mouse.get_pos()))



    def change_color(self, c:np.ndarray):
        self._color = self.color
        self._new_color = c
        if self.color_tween is not None:
            self.color_tween.reset()

    def change_position(self, p:np.ndarray):
        self._center_pos = self.center_pos
        self._new_center_pos = p
        if self.pos_tween is not None:
            self.pos_tween.reset()