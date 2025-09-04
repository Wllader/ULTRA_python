import pygame as pg, numpy as np
from GameController import GameController
from tween import Tween


class Square(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, init_center_pos:np.ndarray, tween:Tween = None, *groups):
        super().__init__(*groups)
        self.gc = GameController()

        self.screen = screen
        self._color = np.random.randint(0, 256, 3)
        self._new_color = self._color.copy()
        self._image = pg.Surface((50, 50))
        self._image.fill(self._color)

        self._center_pos = np.array(init_center_pos)
        self._new_center_pos = self._center_pos.copy()
        self._rect = self._image.get_rect(center=self._center_pos)
        self.mk_held = [False, False, False]

        self.tween = tween if tween else Tween(1000)

    @property
    def rect(self):
        self._rect = self._image.get_rect(center=self.position)
        return self._rect

    @property
    def position(self):
        if (self._center_pos != self._new_center_pos).all():
            p, s = self.tween.get_state(self._center_pos, self._new_center_pos)
            if s:
                self._center_pos = self._new_center_pos
                return self._new_center_pos
            
            return p
        
        else:
            return self._center_pos
        

    @property
    def image(self):
        self._image.fill(self.color)
        return self._image
    
    @property
    def color(self):
        if (self._color != self._new_color).all():
            c, s = self.tween.get_state(self._color, self._new_color)
            if s:
                self._color = self._new_color
                return self._new_color
            
            return c
        
        else:
            return self._color

    def update(self):
        if self.clicked(1):
            self.kill()

        if self.clicked(2):
            self._new_color = np.random.randint(0, 256, 3)
            self.tween.reset()

        return super().update()
    
    def clicked(self, button):
        if (p := pg.mouse.get_pressed()[button]) and not self.mk_held[button] and self.rect.collidepoint(pg.mouse.get_pos()):
            self.mk_held[button] = True
            return True
        elif not p:
            self.mk_held[button] = False
            return False
        
    def change_position(self, pos):
        self._new_center_pos = np.array(pos)
        self.tween.reset()

        