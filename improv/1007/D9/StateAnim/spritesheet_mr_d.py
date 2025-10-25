import pygame as pg, numpy as np


class SpriteSheet:
    def __init__(self, path:str, size:tuple[int], scale:float=1., default_index:tuple[int]=(0, 0)):
        self.sheet = pg.image.load(path).convert_alpha()
        self.size = np.array(size)
        self.scale = scale
        self.default_index = default_index

        self.animations:dict[str, np.ndarray[np.ndarray]] = dict()
        self.animation_state:str = None
        self.current_animation:np.ndarray[np.ndarray] = np.array([0, 0])

        self.clock = pg.time.Clock()
        self.frame_time = 250
        self.frame_index = 0
        self.current_frame_time = 0


    def get_image(self, index:tuple[int]=None):
        if index is None: index = self.default_index
        index = np.array(index)

        image = pg.Surface(self.size, pg.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (*index*self.size, *self.size))

        if self.scale != 1:
            image = pg.transform.scale_by(image, self.scale)

        return image

    def add_animation(self, name:str, frames:list[np.ndarray]):
        self.animations[name.lower()] = frames

    def set_animation(self, name:str, frame_time:int=None):
        name = name.lower()
        if name == self.animation_state: return
        if frame_time is not None: self.frame_time = frame_time

        self.animation_state = name
        self.current_animation = self.animations[name]
        self.frame_index = 0


    @property
    def frame(self):
        if not self.animation_state:
            return self.get_image()
        
        self.current_frame_time += self.clock.tick()
        # while self.current_frame_time >= self.frame_time:
        #     self.current_frame_time -= self.frame_time
        #     self.frame_index = (self.frame_index + 1) % len(self.current_animation)

        if self.current_frame_time >= self.frame_time:
            index_diff = self.current_frame_time // self.frame_time
            self.current_frame_time %= self.frame_time
            self.frame_index = (self.frame_index + index_diff) % len(self.current_animation)


        frame_indicies = self.current_animation[self.frame_index]
        return self.get_image(frame_indicies)

