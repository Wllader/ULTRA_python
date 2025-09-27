import pygame as pg, numpy as np
from game_controller import GameController
from spritesheet_mr_d import SpriteSheet

pg.init()

SIZE = W, H = np.array([600, 600])
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Dinos!")

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0



gc = GameController()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #Update

    #Draw
    screen.fill(GREY * 28)

    pg.display.flip()
    gc.tick(144, 10)

pg.quit()