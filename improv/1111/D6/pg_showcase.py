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
pg.display.set_caption("My first game")
clock = pg.time.Clock()

p = Square(
    screen,
    (50, 100),
    (60, 60)
)

p2 = Square(
    screen,
    (200, 50),
    (100, 100),
    (56, 128, 200)
)

p3 = Square(
    screen,
    (500, 500),
    (20, 20),
    (86, 12, 155),
    (7, 7)
)

g_squares = pg.sprite.Group(
    p, p2, p3
)

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
