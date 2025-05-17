import pygame as pg, numpy as np
from GameController import GameController
from sqaure import Square
from tween import Tween

pg.init()
SIZE = W, H = np.array([600, 600])
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Demo")
CENTER = SIZE / 2

mk_held = False
def click(button, held:bool):
    clicked = pg.mouse.get_pressed()[button]
    out = False
    if clicked and not held:
        held = True
        out = True

    if not clicked:
        held = False

    return out, held

g_squares = pg.sprite.Group()

gc = GameController()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #Updating
    keys = pg.key.get_pressed()
    mkeys = pg.mouse.get_pressed()
    c, mk_held = click(0, mk_held)
    if c:
        g_squares.add(
            Square(
                screen,
                pg.mouse.get_pos(),
                tween=Tween(1000, lambda t: t**6)
            )
        )

    g_squares.update()

    # Drawing
    screen.fill((58, 58, 58))
    g_squares.draw(screen)

    pg.display.flip()
    gc.tick(144, 2)

pg.quit()


    
