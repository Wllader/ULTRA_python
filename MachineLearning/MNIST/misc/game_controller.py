from pygame.time import Clock

class GameController:
    def __init__(self):
        self.running = True
        self.clock = Clock()
        self.dt = 0

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(GameController, cls).__new__(cls)

        return cls.instance

    def tick(self, fps:int=0, factor:int=1):
        self.dt = self.clock.tick(fps) / factor

    def stop(self):
        self.running = False