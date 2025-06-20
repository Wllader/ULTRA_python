import pygame as pg, numpy as np

class SpriteSheet: #? Also is MultiRank
    """Saves just coordinates of frames for it's animations and dynamically renders them from the sprite sheet file when needed."""

    def __init__(self, path:str, size:np.ndarray, scale:float = 1., default_frame:np.ndarray = np.zeros(2, dtype=int), color_key:np.ndarray = None):
        self.sheet = pg.image.load(path).convert_alpha()
        self.size = size
        self.scale = scale
        self.default_frame = default_frame
        self.color_key = color_key

        self.animations:dict[str, list[np.ndarray]] = dict()
        self.animation_state = None
        self.current_animation_lenght = 1

        self.clock = pg.time.Clock()
        self.frame_time = 250
        self.frame_index = 0
        self.current_frame_time = 0


    def get_image(self, frame:np.ndarray = None, color_key:np.ndarray=None):
        if frame is None: frame = self.default_frame
        if color_key is None: color_key = self.color_key

        image = pg.Surface(self.size).convert_alpha()
        image.blit(self.sheet, (0, 0), (*frame*self.size, *self.size))

        if self.scale != 1:
            image = pg.transform.scale_by(image, self.scale)

        if color_key is not None:
            image.set_colorkey(color_key)

        return image
    
    def add_animation(self, name:str, frames:list[np.ndarray], color_key=None):
        self.animations[name] = frames

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
        if self.current_frame_time >= self.frame_time:
            index_difference = self.current_frame_time // self.frame_time
            self.current_frame_time %= self.frame_time
            self.frame_index = (self.frame_index + index_difference) % self.current_animation_lenght

        frame_indicies = self.animations[self.animation_state][self.frame_index]
        return self.get_image(frame_indicies)