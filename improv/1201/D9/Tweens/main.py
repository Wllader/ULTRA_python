import pygame as pg, numpy as np
from game_controller import GameController
from square import Square, ClickState

pg.init()

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

SIZE = W, H = np.array([600, 600])
CENTER = SIZE / 2

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Interpolation demo")
gc = GameController()
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

#! GameLoop
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

    if pg.key.get_pressed()[pg.K_SPACE]:
        for sq in g_squares:
            sq:Square
            sq.position = pg.mouse.get_pos()

    #Draw
    screen.fill(GREY * 28)
    g_squares.draw(screen)

    pg.display.flip()
    gc.tick(144)

pg.quit()


#Todo
# Kliknutí LMB: Vytvoření nového Square s náhodnou barvou
# Kliknutí RMB na existující square: Square změní barvu na jinou náhodnou
# Kliknutí MMB na existující square: Square je odstraněn (self.kill())
# Stisknutí SPACE Všechny existující Square změní svou center lokaci na současnou pozici kurzoru myši