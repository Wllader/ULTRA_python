import pygame as pg
import numpy as np
import pandas as pd
import requests

from widgets import *


pg.init()
SIZE = W, H = np.array([800, 600])
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("CryptoCheck")

GREY = np.ones(3)
WHITE = GREY * 255
BLACK = np.zeros(3)


e_tick = Entry(screen, np.array((10, 10)), np.array((150, 40)), default_text="random")
e_days = Entry(screen, np.array((170, 10)), np.array((70, 40)), default_text="5")
e_gran = Entry(screen, np.array((250, 10)), np.array((100, 40)), default_text="50")

entries = pg.sprite.Group(
    e_tick,
    e_days,
    e_gran
)

widgets = pg.sprite.Group(
    entries,
    Button(screen, np.array((10, 60)), np.array((150, 40)), "Click me!", command=lambda: print(e_tick.text)),
)

#! Game loop
running = True
clock = pg.time.Clock()

while running:
    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        else:
            # Update
            widgets.update(event)
        

    screen.fill(GREY * 56)

    # Draw
    widgets.draw(screen)


    pg.display.flip()
    clock.tick(60)

pg.quit()

