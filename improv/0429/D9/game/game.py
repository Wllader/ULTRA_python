import pygame as pg, numpy as np
from GameController import GameController
from game_entities import *

pg.init()
SIZE = W, H = np.array((1024, 800))
CENTER = SIZE / 2
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Game")

d = Dinosaur(
    screen,
    np.array([24*4, CENTER[1]]),
    SpriteSheet(
        "Sprites\DinoSprites - vita.png",
        np.array([24, 24]),
        4,
        # (0, 0, 0)
    ),
    5
    )

b = Entity(
    screen,
    CENTER,
    SpriteSheet(
        "Sprites/Box.png",
        np.array([32, 32]),
        2
    )

)

d.sheet.add_animation("idle", list(range(4)))
d.sheet.set_animation("idle")

d.sheet.add_animation("walk", list(range(4, 4+6)))
d.sheet.set_animation("walk", 150)

g_dinosaurs = pg.sprite.Group(d)
g_obstacles = pg.sprite.Group(b)

d.collisions = g_obstacles

gc = GameController()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((28, 28, 28))

    g_dinosaurs.update()
    g_obstacles.update()

    g_obstacles.draw(screen)
    g_dinosaurs.draw(screen)

    pg.display.flip()
    gc.tick(144, 10)

pg.quit()