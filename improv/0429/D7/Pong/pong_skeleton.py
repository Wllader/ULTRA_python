import pygame as pg, numpy as np
from PongEntities import PongPlayer, PongBot, PongBall, PongBotAdvanced
from GameController import GameController
from SpriteSheet import SpriteSheet

# Initialize
pg.init()

# Screen dimensions
SIZE = WIDTH, HEIGHT = np.array([800, 600])
CENTER = SIZE / 2
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Pong!")

bg = pg.image.load("Sprites/Bg.png")
bg = pg.transform.scale_by(bg, .78125)

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
player1 = PongBotAdvanced(
    screen,
    PADDLE_DIMS,
    np.array([50, CENTER[1]]),
    paddle_speed,
    (0, 255, 0),
    SpriteSheet(
        "Sprites/Paddle.png",
        np.array([5, 50]),
        2
    )
)

player2 = PongBotAdvanced(
    screen,
    PADDLE_DIMS,
    np.array([WIDTH - 50 - PW, CENTER[1]]),
    paddle_speed,
    (255, 0, 0),
    SpriteSheet(
        "Sprites/Paddle.png",
        np.array([5, 50]),
        2,
        init_frame=1
    )
)

ball = PongBall(
    screen,
    BALL_SIZE,
    CENTER,
    ball_speed,
    WHITE
)

player1.ball = ball
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
    g_entities.update()

    # Drawing
    screen.fill(BLACK)
    screen.blit(bg, (0, 0))

    pg.draw.aaline(screen, WHITE, (CENTER[0], 0), (CENTER[0], HEIGHT))
    screen.blit(*get_score())

    g_entities.draw(screen)

    pg.display.flip()
    gc.tick(144, 10)


pg.quit()