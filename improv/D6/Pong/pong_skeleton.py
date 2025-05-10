import pygame as pg, numpy as np
from PongEntities import PongPlayer, PongBot, PongBall

# Initialize
pg.init()

# Screen dimensions
SIZE = WIDTH, HEIGHT = np.array([800, 600])
CENTER = SIZE / 2
screen = pg.display.set_mode(SIZE)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game objects
PADDLE_DIMS = PW, PH = np.array([10, 100])
BALL_SIZE = np.array([16, 16])

# Speeds
paddle_speed = np.array([0, 5])
ball_speed = np.array([5, 7])

# Positions
player1 = PongPlayer(
    screen,
    PADDLE_DIMS,
    np.array([50, CENTER[1]]),
    paddle_speed,
    WHITE
)

player2 = PongBot(
    screen,
    PADDLE_DIMS,
    np.array([WIDTH - 50 - PW, CENTER[1]]),
    paddle_speed,
    WHITE
)

ball = PongBall(
    screen,
    BALL_SIZE,
    CENTER,
    ball_speed,
    WHITE
)

player2.ball = ball

# Groups
g_entities = pg.sprite.Group(
    player1,
    player2,
    ball
)

g_paddles = pg.sprite.Group(
    player1,
    player2
)

ball.bounce_group = g_paddles

#! Game loop

clock = pg.time.Clock()
dt = 0

running = True
while running:
    # Quit game
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False

    # Update game state
    g_entities.update(dt=dt)

    # Drawing
    screen.fill(BLACK)
    pg.draw.aaline(screen, WHITE, (CENTER[0], 0), (CENTER[0], HEIGHT))
   
    g_entities.draw(screen)

    pg.display.flip()
    dt = clock.tick(144) / 10


pg.quit()