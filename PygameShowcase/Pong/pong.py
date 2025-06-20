import pygame as pg, numpy as np
from PongEntities import *

# Initialize
pg.init()

# Screen dimensions
SIZE = WIDTH, HEIGHT = np.array([800, 600])
CENTER = SIZE / 2
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Pong")

bg = pg.image.load("Sprites/Bg.png")
bg = pg.transform.scale_by(bg, 0.78125)


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game objects
PADDLE_DIMS = PW, PH = np.array([10, 100])
BALL_SIZE = np.array([15, 15])
font = pg.font.Font('freesansbold.ttf', 32)

# Speeds
paddle_speed = np.array([0, 5])
ball_speed = np.array([5, 7])



# Entities
player1 = PongBotAdvanced(
    screen,
    PADDLE_DIMS,
    np.array([55, CENTER[1]]),
    paddle_speed,
    (0, 255, 0),
    SpriteSheet(
        "Sprites/Paddle.png",
        np.array([5, 50]),
        2,
        color_key=BLACK
    )
)

player2 = PongBotAdvanced(
    screen,
    PADDLE_DIMS,
    np.array([WIDTH - 55, CENTER[1]]),
    paddle_speed,
    (255, 0, 0),
    SpriteSheet(
        "Sprites/Paddle.png",
        np.array([5, 50]),
        2,
        color_key=BLACK
    ))

ball = PongBall(
    screen,
    BALL_SIZE,
    CENTER,
    ball_speed,
    WHITE,
    SpriteSheet(
        "Sprites/Ball.png",
        np.array([16, 16]),
        1,
        color_key=BLACK
    )
)

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
ball.sheet.add_animation("shimmer", range(4))
ball.sheet.set_animation("shimmer", 250)
player1.ball = ball
player2.ball = ball
player2.sheet.frame_index = 1

# Score:
game_controller = GameController()

def score_counter():
    score_text = f"{game_controller.get_score(0)}   {game_controller.get_score(1)}"
    score = font.render(score_text, True, WHITE)
    score_rect = score.get_rect()
    score_rect.center = CENTER

    return score, score_rect

#! Game loop
running = True
while running:
    # Quit game
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False
    
    g_entities.update()

    # Drawing
    screen.fill((58, 58, 58))
    screen.blit(bg, (0,0))
    pg.draw.aaline(screen, WHITE, (CENTER[0], 0), (CENTER[0], HEIGHT))
    screen.blit(*score_counter())

    
    g_entities.draw(screen)


    pg.display.flip()
    game_controller.tick(144, 10)


pg.quit()

#~ todo Exact calculations for bots
#todo 5x50 sprite for paddles
#~ todo Clock to GameController