import pygame as pg, numpy as np
from pong_entities import PongPlayer, PongBall

# Initialize
pg.init()

# Screen dimensions
SIZE = W, H = np.array([800, 600])
CENTER = SIZE / 2
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Pong!")

# Colors
GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

# Game objects
PADDLE_DIMS = PW, PH = np.array([10, 100])
BALL_SIZE = np.array([16, 16])

paddle_speed = np.array([0, 7])
ball_speed = np.array([5, 5])


p1 = PongPlayer(
    screen,
    PADDLE_DIMS,
    np.array([55, CENTER[1]]),
    paddle_speed,
    np.array([0, 255, 0])
)

p2 = PongPlayer(
    screen,
    PADDLE_DIMS,
    np.array([W - 55, CENTER[1]]),
    paddle_speed,
    np.array([255, 0, 0])
)

ball = PongBall(
    screen,
    BALL_SIZE,
    CENTER,
    ball_speed,
    WHITE
)

g_paddles = pg.sprite.Group(
    p1, p2
)

ball.g_bounce = g_paddles.copy()

g_entities = pg.sprite.Group(
    p1, ball, p2
)


#! Game loop

clock = pg.time.Clock()
dt = 0
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    # Update game state
    g_entities.update(dt=dt)


    # Draw
    screen.fill(GREY * 18)
    g_entities.draw(screen)

    pg.display.flip()
    dt = clock.tick(144) / 10


pg.quit()