import pygame as pg, numpy as np
from game_controller import GameController


pg.init()

SIZE = W, H = np.array([600, 600])
CENTER = SIZE / 2

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Interpolation demo")

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

g_squares = pg.sprite.Group()

#! Game loop
gc = GameController()
while gc.running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gc.stop()

    #Update

    #Draw
    screen.fill(GREY * 28)

    pg.display.flip()
    gc.tick(144)


pg.quit()