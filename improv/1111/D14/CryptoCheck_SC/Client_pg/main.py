import pygame as pg, numpy as np
from game_controller import GameController
import logging, requests, pandas as pd
from plot import *

from widgets import *


GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

pg.init()
SIZE = W, H = np.array([800, 600])
screen = pg.display.set_mode(SIZE)
logger = logging.getLogger(__name__)
gc = GameController()

plot = Plot(screen, (10, 60), (W-20, H-70))


e_tick = Entry(screen, (10, 10), (150, 40), default_text="random", placeholder_text="Coin tick")
e_days = Entry(screen, (170, 10), (70, 40), default_text="5", placeholder_text="#Days")
e_gran = Entry(screen, (250, 10), (100, 40), default_text="50", placeholder_text="Granularity")


g_entries = pg.sprite.Group(
    e_tick, e_days, e_gran
)


g_widgets = pg.sprite.Group(
    Button(screen, (360, 10), (150, 40), text="Click me!"),
    g_entries,
    plot
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