import pygame as pg, numpy as np


class SpriteSheet:
    def __init__(self, path:str, size:np.ndarray, scale:float = 1., color_key = None, init_frame = 0):
        self.sheet = pg.image.load(path).convert_alpha()
        self.size = size
        self.scale = scale
        self.color_key = color_key
        self.init_frame = init_frame

        self.clock = pg.time.Clock()
        self.frame_time = ...
        self.frame_index = ...
        self.current_frame_time = ...

    def get_image(self, frame:int, color_key=None):
        if color_key is None: color_key = self.color_key

        image = pg.Surface(self.size).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * self.size[0], 0, *self.size))
        if self.scale != 1:
            image = pg.transform.scale_by(image, self.scale)

        if color_key is not None:
            image.set_colorkey(color_key)

        return image
