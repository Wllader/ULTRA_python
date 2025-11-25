import pygame as pg, numpy as np
from square import Square, MovingSquare, PlayerSquare

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
pg.display.set_caption("My first game")
clock = pg.time.Clock()

s = Square(
    screen,
    (50, 200),
    (60, 60)
)

ms_1 = MovingSquare(
    screen,
    (200, 200),
    (40, 40),
    (56, 128, 200),
    (3, 0)
)

ms_2 = MovingSquare(
    screen,
    (300, 300),
    (60, 60),
    (150, 128, 100),
    (0, 2)
)

p = PlayerSquare(
    screen,
    (500, 500),
    (20, 20),
    (86, 12, 155),
    (7, 7)
)

g_squares = pg.sprite.Group(
    s, ms_1, ms_2, p
)

ms_1.collision_group.add(p, ms_2, s)
ms_2.collision_group.add(p, ms_1, s)

#! Game loop
running = True
dt = 0
while running:
    # Event-management
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
