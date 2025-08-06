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
WHITE = GREY * 255
BLACK = GREY * 0


mk_held = np.zeros(3, dtype=bool)
def click(button:int) -> bool:
    out = False
    clicked = pg.mouse.get_pressed()[button]
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


    # Update
    g_squares.update()

    if click(0):
        g_squares.add(
            Square(
                screen,
                np.array(pg.mouse.get_pos())
            )
        )

    if click(2):
        mpos = pg.mouse.get_pos()

        clicked_squares = np.array(
            [ s.rect.collidepoint(mpos) for s in g_squares ],
            dtype=bool
        )

        if not clicked_squares.any():
            for s in g_squares:
                s:Square
                s.change_pos(np.array(mpos))


    # Draw
    screen.fill(GREY * 28)
    g_squares.draw(screen)


    pg.display.flip()
    # Delta-time
    gc.tick(144, 10)

pg.quit()