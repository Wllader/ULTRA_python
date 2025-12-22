import pygame as pg, numpy as np
from game_controller import GameController

pg.init()

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

SIZE = W, H = np.array([600, 600])
CENTER = SIZE / 2

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Interpolation demo")
gc = GameController()


#! GameLoop
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


#Todo
# Kliknutí do volné oblasti: Vytvoření nového Square s náhodnou barvou
# Kliknutí LMB na existující square: Square změní barvu na jinou náhodnou
# Kliknutí MMB na existující square: Square je odstraněn (self.kill())
# Stisknutí SPACE Všechny existující Square změní svou center lokaci na současnou pozici kurzoru myši