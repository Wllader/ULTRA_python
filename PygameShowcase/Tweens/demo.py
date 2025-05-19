import pygame as pg, numpy as np
from GameController import GameController
from Square import Square

pg.init()
scr_size = np.array([600, 600])
screen = pg.display.set_mode(scr_size)
CENTER = scr_size / 2

sq_size = np.array([50, 50])
mk_held = False

g_entities = pg.sprite.Group()

gc = GameController()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    mk = pg.mouse.get_pressed()
    if mk[0] and not mk_held:
        mk_held = True
        g_entities.add(
            Square(screen, pg.mouse.get_pos(), speed=0)
        )

    if not mk[0]:
        mk_held = False

    screen.fill((58, 58, 58))

    g_entities.update()
    g_entities.draw(screen)

    pg.display.flip()
    gc.tick(144, 2)

pg.quit()