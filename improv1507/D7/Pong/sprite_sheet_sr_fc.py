import pygame as pg, numpy as np


class SpriteSheet:
    def __init__(self, path:str, size:tuple[int], scale:float = 1., default_index:int = 0):
        self.sheet = pg.image.load(path).convert_alpha()
        self.size = np.array(size)
        self.scale = scale
        self.default_index = default_index

        self.animations:dict[str, list[pg.Surface]] = dict()
        self.animation_state = None
        self.current_anim_len = 1

        self.clock = pg.time.Clock()
        self.frame_time = 250
        self.frame_index = 0
        self.current_frame_time = 0


    def get_image(self, index:int = None):
        if index is None: index = self.default_index

        image = pg.Surface(self.size, pg.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (index * self.size[0], 0, *self.size))

        if self.scale != 1:
            image = pg.transform.scale_by(image, self.scale)

        return image
    
    def add_animation(self, name:str, frames:list[int]):
        self.animations[name.lower()] = [ self.get_image(fi) for fi in frames ]

    def set_animation(self, name:str, frame_time:int = None):
        if frame_time is not None: self.frame_time = frame_time
        name = name.lower()

        self.animation_state = name
        self.current_anim_len = len(self.animations[name])

    @property
    def frame(self):
        if not self.animation_state:
            return self.get_image()
        
        self.current_frame_time += self.clock.tick()
        # while self.current_frame_time >= self.frame_time:
        #     self.current_frame_time -= self.frame_time
        #     self.frame_index = (self.frame_index + 1) % self.current_anim_len

        if self.current_frame_time >= self.frame_time:
            index_diff = self.current_frame_time // self.frame_time
            self.current_frame_time %= self.frame_time
            self.frame_index = (self.frame_index + index_diff) % self.current_anim_len

        return self.animations[self.animation_state][self.frame_index]