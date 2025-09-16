import pygame as pg, numpy as np

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


p = pg.Rect(
    50, 100, 35, 35
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
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        p.top -= player_speed * dt
    if keys[pg.K_s]:
        p.top += player_speed * dt

    if keys[pg.K_a]:
        p.left -= player_speed * dt
    if keys[pg.K_d]:
        p.left += player_speed * dt


    # Draw
    screen.fill(GREY * 56)
    pg.draw.rect(screen, (255, 0, 0), p)


    pg.display.flip()
    dt = clock.tick(144) / 10



pg.quit()