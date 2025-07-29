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
pg.display.set_caption("My first game")

clock = pg.time.Clock()


p = PlayerSquare(
    screen,
    np.array([50, 50]),
    np.array([50, 50])
)

p2 = MovingSquare(
    screen,
    init_pos=np.array([250, 250]),
    size=np.array([50, 50]),
    color=np.array([200, 160, 48]),
    speed=np.array([5, 0])
)

p3 = MovingSquare(
    screen,
    init_pos=np.array([250, 250]),
    size=np.array([50, 50]),
    color=np.array([48, 160, 200]),
    speed=np.array([0, 5])
)




players = pg.sprite.Group(
    p, p2, p3
)

p.collision_group = pg.sprite.Group(p2, p3)
p2.collision_group = pg.sprite.Group(p, p3)
p3.collision_group = pg.sprite.Group(p, p2)


#! Game loop
running = True
dt = 0
while running:
    # Event-management
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Update
    players.update(dt=dt)

    # Draw
    screen.fill(GREY * 28)

    players.draw(screen)

    pg.display.flip()
    dt = clock.tick(144) / 10

pg.quit()