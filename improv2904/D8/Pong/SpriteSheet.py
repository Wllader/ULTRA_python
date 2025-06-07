import pygame as pg, numpy as np


class SpriteSheet:
    def __init__(self, path:str, size:np.ndarray, scale:float = 1., color_key = None, init_frame = 0):
        self.sheet = pg.image.load(path).convert_alpha()
        self.size = size
        self.scale = scale
        self.color_key = color_key
        self.init_frame = init_frame

        self.animations:dict[str, list[pg.Surface]] = dict()
        self.animation_state = None
        self.current_animation_lenght = 1

        self.clock = pg.time.Clock()
        self.frame_time = 250
        self.frame_index = 0
        self.current_frame_time = 0

    def get_image(self, frame:int, color_key=None):
        if color_key is None: color_key = self.color_key

        image = pg.Surface(self.size).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * self.size[0], 0, *self.size))
        if self.scale != 1:
            image = pg.transform.scale_by(image, self.scale)

        if color_key is not None:
            image.set_colorkey(color_key)

        return image
    
    def add_animation(self, name:str, frames:list[int], color_key=None):
        self.animations[name] = [ self.get_image(f, color_key) for f in frames ]

    def set_animation(self, name:str, frame_time=None):
        if frame_time: self.frame_time = frame_time
        self.animation_state = name
        self.current_animation_lenght = len(self.animations[name])

    @property
    def frame(self):
        if not self.animation_state:
            return self.get_image(self.init_frame)
        
        self.current_frame_time += self.clock.tick()
        if self.current_frame_time >= self.frame_time:
            index_difference = self.current_frame_time // self.frame_time
            self.current_frame_time %= self.frame_time
            self.frame_index = (self.frame_index + index_difference) % self.current_animation_lenght

        # while self.current_frame_time >= self.frame_time:
        #     self.current_frame_time -= self.frame_time
        #     self.frame_index = (self.frame_index + 1) % self.current_animation_lenght
        
        return self.animations[self.animation_state][self.frame_index]

