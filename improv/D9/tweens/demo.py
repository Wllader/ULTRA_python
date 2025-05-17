import pygame as pg, numpy as np
from GameController import GameController
from sqaure import Square
from tween import Tween

pg.init()
SIZE = W, H = np.array([600, 600])
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Demo")
CENTER = SIZE / 2

mk_held = [False, False, False]
def click(button):
    clicked = pg.mouse.get_pressed()[button]
    out = False
    if clicked and not mk_held[button]:
        mk_held[button] = True
        out = True

    if not clicked:
        mk_held[button] = False

    return out

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
    if click(0):
        g_squares.add(
            Square(
                screen,
                pg.mouse.get_pos(),
                tween=Tween.EaseInOutBounce(1000)
            )
        )

    if click(2):
        mpos = pg.mouse.get_pos()

        clicked_squares = np.array(
            [ s.rect.collidepoint(mpos) for s in g_squares ],
            dtype=bool
        )

        if (~clicked_squares).all():
            for s in g_squares:
                s:Square
                s.change_position(mpos)


    g_squares.update()

    # Drawing
    screen.fill((58, 58, 58))
    g_squares.draw(screen)

    pg.display.flip()
    gc.tick(144, 2)

pg.quit()


    
