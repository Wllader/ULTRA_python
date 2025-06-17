import pygame as pg, numpy as np

class SpriteSheet:
    def __init__(self, path:str, size:np.ndarray, scale:float = 1., default_frame:int = 0):
        self.sheet = pg.image.load(path).convert_alpha()
        self.size = size
        self.scale = scale
        self.default_frame = default_frame

        self.clock = pg.time.Clock()
        self.frame_time = ...
        self.frame_index = ...
        self.current_frame_time = ...


    def get_image(self, frame:int = None, color_key:np.ndarray=None):
        if frame is None: frame = self.default_frame

        image = pg.Surface(self.size).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * self.size[0], 0, *self.size))

        if self.scale != 1:
            image = pg.transform.scale_by(image, self.scale)

        if color_key is not None:
            image.set_colorkey(color_key)

        return image