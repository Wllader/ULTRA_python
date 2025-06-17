import pygame as pg, numpy as np
from pong_entities import PongPlayer, PongBot, PongBall
from game_controller import GameController
from sprite_sheet import SpriteSheet

# Initialize
pg.init()

# Screen dimensions
SIZE = W, H = np.array([800, 600])
CENTER = SIZE / 2
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Pong!")

bg = pg.image.load("Sprites/Bg.png")
bg = pg.transform.scale_by(bg, .78125)

# Colors
GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

# Game objects
PADDLE_DIMS = PW, PH = np.array([10, 100])
BALL_SIZE = np.array([16, 16])

paddle_speed = np.array([0, 5])
ball_speed = np.array([5, 7])


p1 = PongBot(
    screen,
    PADDLE_DIMS,
    np.array([55, CENTER[1]]),
    paddle_speed,
    np.array([0, 255, 0]),
    SpriteSheet(
        "Sprites/Paddle.png",
        np.array([5, 50]),
        2
    )
)

p2 = PongBot(
    screen,
    PADDLE_DIMS,
    np.array([W - 55, CENTER[1]]),
    paddle_speed,
    np.array([255, 0, 0]),
    SpriteSheet(
        "Sprites/Paddle.png",
        np.array([5, 50]),
        2,
        1
    )
)

ball = PongBall(
    screen,
    BALL_SIZE,
    CENTER,
    ball_speed,
    WHITE,
    SpriteSheet(
        "Sprites/Ball.png",
        np.array([16, 16]),
        1
    )
)

p1.target = ball
p2.target = ball

g_paddles = pg.sprite.Group(
    p1, p2
)

ball.g_bounce = g_paddles.copy()

g_entities = pg.sprite.Group(
    p1, ball, p2
)


#! Game loop

gc = GameController()
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    # Update game state
    g_entities.update()


    # Draw
    screen.fill(GREY * 18)
    screen.blit(bg, (0, 0))

    g_entities.draw(screen)

    pg.display.flip()
    gc.tick(144, 10)


pg.quit()