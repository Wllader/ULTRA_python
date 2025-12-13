import pygame as pg, numpy as np
from square import Square

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

p1 = Square(
    screen,
    (0, 50),
    (100, 50),
    WHITE
)
p2 = Square(
    screen,
    (0, 150),
    (100, 50),
    (255, 0, 0)
)
p3 = Square(
    screen,
    (0, 300),
    (100, 50),
    (0, 255, 0)
)


g_squares = pg.sprite.Group(
    p1, p2, p3
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
    dt = clock.tick(60) / 10

pg.quit()