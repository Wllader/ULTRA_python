import pygame as pg, numpy as np
from game_controller import GameController
from enum import Enum, auto


class ClickState(Enum):
    CLICKED = auto()
    HELD = auto()
    RELEASED = auto()
    MISSED = auto()


class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, init_center_pos:tuple[int]):
        super().__init__()

        self.gc = GameController()
        ...


    def click(self, button:int) -> ClickState:
        pg.mouse.get_pressed()
        pg.mouse.get_pos()
        ...

class Square(Entity):
    ...