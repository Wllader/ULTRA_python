import pygame as pg, numpy as np
from game_controller import GameController
from spritesheet_mr_d import SpriteSheet
from game_entities import Dino

pg.init()

GREY = np.ones(3, dtype=np.uint8)
BLACK = GREY * 0
WHITE = GREY * 255
SIZE = W, H = np.array([600, 600])

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Dinos!")
gc = GameController()


d = Dino(
    screen,
    (18, 18),
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


#! GameLoop
while gc.running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gc.stop()

    #Update
    g_dinos.update()

    #Draw
    screen.fill(GREY * 28)
    g_dinos.draw(screen)

    pg.display.flip()
    gc.tick(144, 10)

pg.quit()

