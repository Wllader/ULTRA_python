import pygame as pg, numpy as np
from game_controller import GameController
from square import Square
from tween import Tween

pg.init()

SIZE = W, H = np.array([600, 600])
CENTER = SIZE / 2

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Interpolation demo")

GREY = np.ones(3, dtype=np.uint8)
BLACK = GREY * 0
WHITE = GREY * 255


mk_held = np.zeros(3, dtype=bool)
def click(button:int):
    clicked = pg.mouse.get_pressed()[button]
    out = False
    if clicked and not mk_held[button]:
        mk_held[button] = True
        out = True

    if not clicked:
        mk_held[button] = False

    return out

g_squares = pg.sprite.Group()

#! Game loop
gc = GameController()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    # Update
    if click(0):
        g_squares.add(
            Square(
                screen,
                np.array(pg.mouse.get_pos()),
                Tween.EaseInOutCubic(500)
            )
        )

    if click(2):
        mpos = pg.mouse.get_pos()

        clicked_squares = np.array(
            [ s.rect.collidepoint(mpos) for s in g_squares ],
            dtype=bool
        )

        #~ if (~clicked_squares).all():
        if not clicked_squares.any():
            for s in g_squares:
                s:Square
                s.change_pos(mpos)


    g_squares.update()

    # Draw
    screen.fill(GREY * 56)

    g_squares.draw(screen)


    pg.display.flip()
    gc.tick(144)

pg.quit()