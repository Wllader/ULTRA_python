import pygame as pg, numpy as np

class SpriteSheet:
    def __init__(self, path:str, size:np.ndarray, scale:float = 1., default_frame:int = 0):
        self.sheet = pg.image.load(path).convert_alpha()
        self.size = size
        self.scale = scale
        self.default_frame = default_frame

        self.animations:dict[str, list[pg.Surface]] = dict()
        self.animation_state = None
        self.current_animation_lenght = 1

        self.clock = pg.time.Clock()
        self.frame_time = 250
        self.frame_index = 0
        self.current_frame_time = 0


    def get_image(self, frame:int = None):
        if frame is None: frame = self.default_frame

        image = pg.Surface(self.size, pg.SRCALPHA)
        image.blit(self.sheet, (0, 0), (frame * self.size[0], 0, *self.size))

        if self.scale != 1:
            image = pg.transform.scale_by(image, self.scale)

        return image
    
    def add_animation(self, name:str, frames:list[int]):
        self.animations[name] = [ self.get_image(f) for f in frames ]

    def set_animation(self, name:str, frame_time:int = None):
        if not frame_time: frame_time = self.frame_time
        else: self.frame_time = frame_time

        self.animation_state = name
        self.current_animation_lenght = len(self.animations[name])

    @property
    def frame(self):
        if not self.animation_state:
            return self.get_image(self.default_frame)
        
        self.current_frame_time += self.clock.tick()
        # while self.current_frame_time >= self.frame_time:
        #     self.current_frame_time -= self.frame_time
        #     self.frame_index = (self.frame_index + 1) % self.current_animation_lenght

        if self.current_frame_time >= self.frame_time:
            index_difference = self.current_frame_time // self.frame_time
            self.current_frame_time %= self.frame_time
            self.frame_index = (self.frame_index + index_difference) % self.current_animation_lenght

        return self.animations[self.animation_state][self.frame_index]