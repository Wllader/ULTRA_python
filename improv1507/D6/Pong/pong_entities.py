import pygame as pg, numpy as np
from enum import Enum, auto


class PongEntity(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()


class PongPlayer(PongEntity):
    pass


class PongBot(PongEntity):
    pass


class PongBall(PongEntity):
    pass