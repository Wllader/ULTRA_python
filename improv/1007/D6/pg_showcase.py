import pygame as pg, numpy as np
from square import Square


# Inicializace
pg.init()


# Definice konstant
GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

SIZE = W, H = np.array([800, 600])
player_speed = 5


# Definice objektů
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()
pg.display.set_caption("My first game")

p = Square(screen, (50, 50), (50, 50), speed=(10, 5))
p2 = Square(screen, (100, 235), (50, 50), color=(255, 0, 0))


g_squares = pg.sprite.Group(
    p, p2
)
p2.collison_group.add(p)
p.collison_group.add(p2)

#! Game loop
running = True
dt = 0
while running:
    # Event-management:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Update
    g_squares.update(dt=dt)


    # Draw
    screen.fill(GREY * 56)
    g_squares.draw(screen)


    pg.display.flip()
    dt = clock.tick(144) / 10

pg.quit()