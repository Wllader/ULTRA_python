import pygame as pg, numpy as np
from square import PlayerSquare, MovingSquare, Square

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


p = PlayerSquare(
    screen,
    np.array([50, 100]),
    np.array([35, 35])
)

s1 = Square(
    screen,
    np.array([100, 100]),
    np.array([35, 35]),
    GREY * 112
)

s2 = MovingSquare(
    screen,
    np.array([80, 200]),
    np.array([35, 35]),
    np.array([0, 255, 255]),
    np.array([5, 0])
)

s2.collision_group.add(p, s1)



g_entities = pg.sprite.Group(
    p, s1, s2
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
    g_entities.update(dt=dt)


    # Draw
    screen.fill(GREY * 56)
    g_entities.draw(screen)



    pg.display.flip()
    dt = clock.tick(144) / 10



pg.quit()