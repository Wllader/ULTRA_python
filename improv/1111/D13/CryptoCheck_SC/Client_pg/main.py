import pygame as pg, numpy as np
from game_controller import GameController
import logging, requests, pandas as pd

from widgets import *


GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

pg.init()
SIZE = W, H = np.array([800, 600])
screen = pg.display.set_mode(SIZE)
logger = logging.getLogger(__name__)
gc = GameController()




g_widgets = pg.sprite.Group(
    Label(screen, (10, 70), (150, 40), text="This is label"),
    Button(screen, (10, 10), (150, 40), text="Click me!"),
    Entry(screen, (170, 10), (150, 40), placeholder_text="Write smthg")
)


#! Game loop
while gc.running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gc.stop()
        else:
            #Update 
            g_widgets.update(event)
            

    #Draw
    screen.fill(GREY * 56)
    g_widgets.draw(screen)


    pg.display.flip()
    gc.tick(144)

pg.quit()