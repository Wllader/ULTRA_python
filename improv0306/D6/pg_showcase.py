# Import a základní inicializace
import pygame as pg, numpy as np
from square import Square, Moving_Square

pg.init()

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

# Inicializace objektů
SIZE = W, H = np.array([800, 600])
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("My first game")

player = Square(
    screen, 
    np.array([200, 200]), 
    np.array([50, 50])
)

p2 = Moving_Square(
    screen,
    np.array([400, 200]),
    np.array([50, 50]),
    GREY*160,
    np.array([10, 10])
)
p2.collission_group.add(player)
player.collission_group.add(p2)


players = pg.sprite.Group(
    player, p2
)


#! Game loop
clock = pg.time.Clock()
dt = 0
running = True
while running:
    # Event-management
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    # Update
    players.update(dt=dt)


    # Vykreslování (Draw)
    screen.fill(GREY * 28)

    players.draw(screen)

    pg.display.flip()
    dt = clock.tick(10) / 10


pg.quit()