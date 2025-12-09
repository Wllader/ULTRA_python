import pygame as pg, numpy as np
from game_controller import GameController
from square import ClickState, Square


pg.init()

SIZE = W, H = np.array([600, 600])
CENTER = SIZE / 2

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Interpolation demo")

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0




mk_held = np.zeros(3, dtype=bool)
def click(button:int) -> ClickState:
    p = pg.mouse.get_pressed()[button]
    h = mk_held[button]

    if p and not h:
        mk_held[button] = True
        return ClickState.CLICKED
    elif p and h:
        return ClickState.HELD
    elif not p and h:
        mk_held[button] = False
        return ClickState.RELEASED
        
    return ClickState.UNKNOWN

g_squares = pg.sprite.Group()

#! Game loop
gc = GameController()
while gc.running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gc.stop()

    #Update
    g_squares.update()
    if click(0) == ClickState.CLICKED:
        g_squares.add(
            Square(
                screen,
                pg.mouse.get_pos()
            )
        )

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        for s in g_squares:
            s:Square
            s.change_position(pg.mouse.get_pos())



    #Draw
    screen.fill(GREY * 28)
    g_squares.draw(screen)

    pg.display.flip()
    gc.tick(144)


pg.quit()