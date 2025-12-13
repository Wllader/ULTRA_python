import pygame as pg, numpy as np
from square import Square, MovingSquare, PlayerSquare

# Inicializace
pg.init()

# Definice konstant
GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

SIZE = W, H = np.array([800, 600])
CENTER = SIZE / 2

player_speed = 5

# Definice objektů
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("My first game")
clock = pg.time.Clock()

p = PlayerSquare(
    screen,
    (0, 50),
    (50, 50),
    WHITE
)

ms = MovingSquare(
    screen,
    CENTER,
    (50, 50),
    (0, 255, 0)
)

s = Square(
    screen,
    (300, 300),
    (50, 50),
    (255, 0, 0)
)

ms.collision_group.add(p, s)


g_squares = pg.sprite.Group(
    p, ms, s
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
    screen.fill(GREY * 16)
    g_squares.draw(screen)
    


    pg.display.flip()
    dt = clock.tick(144) / 10

pg.quit()