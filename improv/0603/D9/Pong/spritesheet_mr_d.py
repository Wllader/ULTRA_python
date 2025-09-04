import pygame as pg, numpy as np

class SpriteSheet:
    def __init__(self, path:str, size:np.ndarray, scale:float = 1., default_frame:np.ndarray = np.zeros(2, dtype=int)):
        self.sheet = pg.image.load(path).convert_alpha()
        self.size = size
        self.scale = scale
        self.default_frame = default_frame

        self.animations:dict[str|int, list[np.ndarray]] = dict()
        self.animation_state = None
        self.current_animation_lenght = 1

        self.clock = pg.time.Clock()
        self.frame_time = 250
        self.frame_index = 0
        self.current_frame_time = 0


    def get_image(self, frame:np.ndarray = None):
        if frame is None: frame = self.default_frame

        image = pg.Surface(self.size, pg.SRCALPHA) #new
        image.blit(self.sheet, (0, 0), (*frame*self.size, *self.size))

        if self.scale != 1:
            image = pg.transform.scale_by(image, self.scale)

        return image
    
    def add_animation(self, name:str, frames:list[np.ndarray]):
        self.animations[name] = frames

    def set_animation(self, name:str, frame_time_ms:int = None):
        if name not in self.animations or name == self.animation_state: return
        if not frame_time_ms: frame_time_ms = self.frame_time
        else: self.frame_time = frame_time_ms

        self.animation_state = name
        self.current_animation_lenght = len(self.animations[name])
        self.frame_index = 0 #new

    @property
    def frame(self):
        if not self.animation_state:
            return self.get_image(self.default_frame)
        
        self.current_frame_time += self.clock.tick()
        if self.current_frame_time >= self.frame_time:
            index_difference = self.current_frame_time // self.frame_time
            self.current_frame_time %= self.frame_time
            self.frame_index = (self.frame_index + index_difference) % self.current_animation_lenght

        frame_indicies = self.animations[self.animation_state][self.frame_index]
        return self.get_image(frame_indicies)