import pygame as pg, numpy as np
from game_controller import GameController
from enum import Enum, auto


class Entity(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, size:tuple[int], init_pos:tuple[int]):
        pass


class Dino(Entity):
    def __init__(self, screen, size, init_pos, spritesheet, speed:float):
        super().__init__(screen, size, init_pos)