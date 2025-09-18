import pygame as pg, numpy as np
from pong_entities import PongPlayer, PongBall, PongBot

pg.init()

#Constants
SIZE = W, H = np.array([800, 600])
CENTER = SIZE / 2

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

PADDLE_DIMS = PW, PH = np.array([10, 100])
PADDLE_SPEED = np.array([0, 5])

BALL_SIZE = np.array([16, 16])
BALL_SPEED = np.array([5, 7])


#Objects
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Pong!")
clock = pg.time.Clock()

player = PongPlayer(
    screen,
    PADDLE_DIMS,
    (55, CENTER[1]),
    PADDLE_SPEED,
    (0, 255, 0)
)

bot = PongBot(
    screen,
    PADDLE_DIMS,
    (W-55, CENTER[1]),
    PADDLE_SPEED,
    (255, 0, 0)
)

ball = PongBall(
    screen,
    BALL_SIZE,
    CENTER,
    BALL_SPEED,
    WHITE
)

g_paddles = pg.sprite.Group(
    player, bot
)

ball.g_bounce = g_paddles

g_entities = pg.sprite.Group(
    ball, g_paddles
)

bot.ball = ball


#! Game Loop
running = True
dt = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #Update
    g_entities.update(dt=dt)

    #Draw
    screen.fill(GREY * 28)
    g_entities.draw(screen)


    pg.display.flip()
    dt = clock.tick(144) / 10


pg.quit()