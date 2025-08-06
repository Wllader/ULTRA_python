import pygame as pg, numpy as np


class SpriteSheet:
    def __init__(self, path:str, size:tuple[int], scale:float = 1., default_frame:tuple[int] = (0, 0)):
        self.sheet = pg.image.load(path).convert_alpha()
        self.size = np.array(size)
        self.scale = scale
        self.default_frame = np.array(default_frame)

        self.animations:dict[str, list[np.ndarray]] = dict()
        self.animation_state = None
        self.current_anim_len = 1

        self.clock = pg.time.Clock()
        self.frame_time = 250
        self.frame_index = 0
        self.current_frame_time = 0


    def get_image(self, frame:tuple[int] = None):
        frame = self.default_frame if frame is None else np.array(frame)

        image = pg.Surface(self.size, pg.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (*frame*self.size, *self.size))

        if self.scale != 1:
            image = pg.transform.scale_by(image, self.scale)

        return image
    
    def add_animation(self, name:str, frames:list[np.ndarray]):
        self.animations[name.lower()] = frames

    def set_animation(self, name:str, frame_time:int = None):
        if frame_time is not None: self.frame_time = frame_time
        name = name.lower()
        if name == self.animation_state: return

        self.animation_state = name
        self.current_anim_len = len(self.animations[name])
        self.frame_index = 0

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

        frame_indicies = self.animations[self.animation_state][self.frame_index]
        return self.get_image(frame_indicies)