import pygame as pg, numpy as np
from square import Square, PlayerSquare, MovingSquare


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

p = PlayerSquare(screen, (50, 50), (50, 50), speed=(6, 6))
p2 = Square(screen, (100, 235), (20, 100), color=(255, 0, 0))
p3 = MovingSquare(screen, (500, 400), (50, 50), (200, 200, 60), (0, 7))


g_squares = pg.sprite.Group(
    p, p2, p3
)

p3.collison_group.add(p, p2)
p2.collison_group.add(p, p3)
p.collison_group.add(p2, p3)


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