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
    np.array([50, 50]),
    np.array([50, 50])
)

players = pg.sprite.Group(
    p,
    Square(
        screen,
        np.array([250, 250]),
        np.array([50, 50]),
        np.array([200, 160, 48])
    )
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
    players.update(dt=dt)

    # Draw
    screen.fill(GREY * 28)

    players.draw(screen)

    pg.display.flip()
    dt = clock.tick(60) / 10

pg.quit()