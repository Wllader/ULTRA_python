import pygame as pg, numpy as np
from game_controller import GameController
from game_entities import Dino
from spritesheet_mr_d import SpriteSheet

pg.init()

SIZE = W, H = np.array([600, 600])
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Dinos!")

GREY = np.ones(3, dtype=np.uint8)
BLACK = GREY * 0
WHITE = GREY * 255


d = Dino(
    screen,
    np.array([15, 15]),
    np.array([50, 50]),
    spritesheet=SpriteSheet(
        "Sprites/Dinos.png",
        np.array([22, 18]),
        4,
        np.array([0, 0])
    )
)

d.sheet.add_animation("idle", [ np.array([i, 0]) for i in range(4) ])
d.sheet.add_animation("walk", [ np.array([i, 0]) for i in range(4, 10) ])

g_dinos = pg.sprite.Group(
    d
)


gc = GameController()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Update
    g_dinos.update()

    # Draw
    screen.fill(GREY * 28)

    g_dinos.draw(screen)

    pg.draw.lines(screen, WHITE, True, [ d.rect.topleft, d.rect.topright, d.rect.bottomright, d.rect.bottomleft])

    pg.display.flip()
    gc.tick(144, 10)

pg.quit()