import pygame as pg, numpy as np, pandas as pd
import requests
from widgets import *



pg.init()
SIZE = W, H = np.array([1000, 600])
screen = pg.display.set_mode(SIZE)

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0


e_tick = Entry(screen, np.array([10, 10]), np.array([150, 40]), default_text="random")
e_days = Entry(screen, np.array([170, 10]), np.array([70, 40]), default_text="5")


entries = pg.sprite.Group(
    e_tick,
    e_days
)

widgets = pg.sprite.Group(
   entries,
   Button(screen, np.array([10, 60]), np.array([150, 40]), "Click me!") 
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

    #Draw
    screen.fill(GREY * 56)
    widgets.draw(screen)


    pg.display.flip()
    clock.tick(144)

pg.quit()