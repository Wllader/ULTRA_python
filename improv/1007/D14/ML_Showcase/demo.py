import pygame as pg, numpy as np
from game_controller import GameController
import logging, requests, pandas as pd

from widgets import *

logging.basicConfig(level=logging.INFO)


GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

pg.init()
SIZE = W, H = np.array([800, 600])
screen = pg.display.set_mode(SIZE)
gc = GameController()


g_widgets = pg.sprite.Group(
    Label(screen, (10, 10), (70, 30), "Ahoj!"),
    CheckBox(screen, (50, 50), (20, 20)),
    Canvas(screen, (100, 100), (280, 280)).disable(),
    b := BarPlot(screen, (200, 200), (300, 300), np.random.randint(0, 50, 20) / 50),
    Button(screen, (80, 10), (80, 30), "Shuffle bars", command=lambda: b.set_data(np.random.randint(0, 50, 20) / 50))
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