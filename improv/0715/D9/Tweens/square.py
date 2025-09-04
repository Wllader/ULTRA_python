import pygame as pg, numpy as np
from game_controller import GameController
from tween import Tween


class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, init_center_pos:tuple[int]):
        super().__init__()

        self.gc = GameController()

        self.screen = screen
        self._image = pg.Surface((50, 50))
        self._rect = self._image.get_rect(center=init_center_pos)

    @property
    def rect(self):
        return self._rect
    
    @property
    def image(self):
        return self._image
    


class Square(Entity):
    def __init__(self, screen, init_center_pos):
        super().__init__(screen, init_center_pos)

        self._color = np.random.randint(0, 256, 3)
        self._new_color = self._color.copy()

        self._center_pos = np.array(init_center_pos)
        self._new_center_pos = self._center_pos.copy()
        
        self._image.fill(self._color)
        self.mk_held = np.zeros(3, dtype=bool)
        self.color_tween = Tween.EaseInElastic(700, clipped=True)
        self.pos_tween = Tween.EaseInElastic(700)

    @property
    def rect(self):
        self._rect = self._image.get_rect(center=self.position)
        return self._rect

    @property
    def position(self):
        if self.pos_tween is None:
            self._center_pos = self._new_center_pos
            return self._center_pos
        
        return self.pos_tween.tweenify(self._center_pos, self._new_center_pos)

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
    
    def update(self):
        if self.click(1):
            self.kill()

        if self.click(2):
            self.change_color(np.random.randint(0, 256, 3))

    def change_pos(self, pos:np.ndarray):
        self._center_pos = self.position
        self._new_center_pos = pos
        if self.pos_tween is not None:
            self.pos_tween.reset()

    def change_color(self, c:np.ndarray):
        self._color = self.color
        self._new_color = c
        if self.color_tween is not None:
            self.color_tween.reset()

    def click(self, button:int) -> bool:
        p = pg.mouse.get_pressed()[button]
        h = self.mk_held[button]
        c = self.rect.collidepoint(pg.mouse.get_pos())

        if p and not h and c:   # Pushed
            self.mk_held[button] = True
            return True
        elif p and h and c:     # Held
            return False
        elif not p and h:       # Released
            self.mk_held[button] = False
            return False
        elif p and not h and not c: # Missed
            return False
