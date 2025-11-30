import pygame as pg, numpy as np
from pong_entities import PongPlayer, PongBot, PongBall, PongBotAdvanced
from game_controller import GameController
from spritesheet_sr_fc import SpriteSheet

# Initialize
pg.init()

# Screen dimensions
SIZE = W, H = np.array([800, 600])
CENTER = SIZE / 2
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Pong!")

bg = pg.image.load("Sprites/Bg.png")
bg = pg.transform.scale_by(bg, W / bg.get_width())

# Colors
GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

# Game objects
PADDLE_DIMS = PW, PH = np.array([10, 100])
BALL_SIZE = np.array([16, 16])
font = pg.font.Font("freesansbold.ttf", 32)



paddle_speed = np.array([0, 5])
ball_speed = np.array([5, 7])


p1 = PongBotAdvanced(
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

p2 = PongBotAdvanced(
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

p1.ball = ball
p2.ball = ball

g_paddles = pg.sprite.Group(
    p1, p2
)

ball.g_bounce = g_paddles.copy()
ball.sheet.add_animation("shimmer", list(range(4)))
ball.sheet.set_animation("shimmer", 250)

g_entities = pg.sprite.Group(
    p1, ball, p2
)

gc = GameController()

#Score
def score_counter():
    score_text = f"{gc.get_score(0)}   {gc.get_score(1)}"
    score = font.render(score_text, True, WHITE)
    score_rect = score.get_rect()
    score_rect.center = CENTER

    return score, score_rect


#! Game loop
while gc.running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gc.stop()


    # Update game state
    g_entities.update()


    # Draw
    screen.fill(GREY * 18)
    screen.blit(bg, (0, 0))

    pg.draw.line(screen, WHITE, (CENTER[0], 0), (CENTER[0], H))
    pg.draw.line(screen, (0, 255, 0), (0,0), (0, H))
    pg.draw.line(screen, (255, 0, 0), (W-1,0), (W-1, H))
    pg.draw.line(screen, WHITE, (0,0), (W, 0))
    pg.draw.line(screen, WHITE, (0,H-1), (W, H-1))
    screen.blit(*score_counter())

    g_entities.draw(screen)


    pg.display.flip()
    gc.tick(144, 10)


pg.quit()