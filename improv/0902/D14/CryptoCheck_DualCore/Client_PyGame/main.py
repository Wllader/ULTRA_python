import pygame as pg, numpy as np
from widgets import Button, Entry
from game_controller import GameController

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

pg.init()
SIZE = W, H = np.array([800, 600])
screen = pg.display.set_mode(SIZE)

entry = Entry(screen, (10, 10), (150, 40), default_text="Example", tooltip_text="text")



g_entries = pg.sprite.Group(
    entry
)

g_widgets = pg.sprite.Group(
    g_entries,
    Button(screen, (10, 60), (150, 40), text="Click me!")
)

#! Game loop
gc = GameController()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        else:
            #Update
            g_widgets.update(event)


    #Draw
    screen.fill(GREY * 56)
    g_widgets.draw(screen)

    pg.display.flip()
    gc.tick(144)

pg.quit()