import pygame as pg, numpy as np
from PongEntities import PongPlayer, PongBot, PongBall
from GameController import GameController

# Initialize
pg.init()

# Screen dimensions
SIZE = WIDTH, HEIGHT = np.array([800, 600])
CENTER = SIZE / 2
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Pong!")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pg.font.Font("freesansbold.ttf", 32)

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
    (0, 255, 0)
)

player2 = PongBot(
    screen,
    PADDLE_DIMS,
    np.array([WIDTH - 50 - PW, CENTER[1]]),
    paddle_speed,
    (255, 0, 0)
)

ball = PongBall(
    screen,
    BALL_SIZE,
    CENTER,
    ball_speed,
    WHITE
)

#player1.ball = ball
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
gc = GameController()

def get_score():
    score_text = f"{gc.get_score(0)}   {gc.get_score(1)}"
    score = font.render(score_text, True, WHITE)
    score_rect = score.get_rect(center=CENTER)

    return score, score_rect

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
    screen.blit(*get_score())

    g_entities.draw(screen)

    pg.display.flip()
    dt = clock.tick(144) / 10


pg.quit()