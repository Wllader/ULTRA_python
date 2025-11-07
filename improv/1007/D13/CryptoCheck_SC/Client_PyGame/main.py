import pygame as pg, numpy as np
from game_controller import GameController
import logging, requests, pandas as pd

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

pg.init()
SIZE = W, H = np.array([800, 600])
screen = pg.display.set_mode(SIZE)
logger = logging.getLogger(__name__)
gc = GameController()





#! Game loop
while gc.running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gc.stop()
    
    #Update

    #Draw
    screen.fill(GREY * 56)

    pg.display.flip()
    gc.tick(144)

pg.quit()