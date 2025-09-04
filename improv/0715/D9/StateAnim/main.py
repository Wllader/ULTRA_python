import pygame as pg, numpy as np
from game_controller import GameController
from sprite_sheet_mr_d import SpriteSheet
from game_entities import Dino

pg.init()

SIZE = W, H = np.array([600, 600])
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Dinos!")

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

d = Dino(
    screen,
    np.array([18, 18]) * 5,
    (100, 50),
    SpriteSheet(
        "Dinos.png",
        (22, 18),
        5
    )
)


g_dinos = pg.sprite.Group(
    d
)

gc = GameController()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #Update
    g_dinos.update()

    #Draw
    screen.fill(GREY * 28)
    g_dinos.draw(screen)


    pg.display.flip()
    #Delte-time
    gc.tick(144, 10)

pg.quit()