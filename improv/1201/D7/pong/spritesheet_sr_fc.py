import pygame as pg, numpy as np

class SpriteSheet:
    def __init__(self, path:str, size:tuple[int], scale:float=1., default_index:int=0):
        self.sheet = pg.image.load(path).convert_alpha()
        self.size = np.array(size)
        self.scale = scale
        self.default_index = default_index

    def get_image(self, index:int=None):
        ...
