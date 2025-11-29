from pygame.time import Clock

class GameController:
    def __init__(self):
        self.clock = Clock()
        self.dt = 0
        self.running = True

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(GameController, cls).__new__(cls)

        return cls.instance

    def tick(self, fps:int, factor:int=1):
        self.dt = self.clock.tick(fps) / factor

    def stop(self):
        self.running = False