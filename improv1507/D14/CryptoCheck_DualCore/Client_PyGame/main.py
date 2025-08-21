import pygame as pg, numpy as np, pandas as pd
import requests

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

pg.init()
SIZE = W, H = np.array([800, 600])
screen = pg.display.set_mode(SIZE)


#! Game loop
running = True
clock = pg.time.Clock()
while running:
    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    #Draw
    screen.fill(GREY * 56)


    pg.display.flip()
    clock.tick(144)

pg.quit()


