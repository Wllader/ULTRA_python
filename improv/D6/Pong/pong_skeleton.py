import pygame as pg, numpy as np
from PongEntities import PongPlayer

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
paddle_speed = np.array([0, 7])
ball_speed = np.array([5, 5])

# Positions
player1 = PongPlayer(
    screen,
    PADDLE_DIMS,
    np.array([50, CENTER[1]]),
    paddle_speed,
    WHITE
)

player2 = PongPlayer(
    screen,
    PADDLE_DIMS,
    np.array([WIDTH - 50 - PW, CENTER[1]]),
    paddle_speed,
    WHITE
)

ball = pg.Rect(
    *((SIZE - BALL_SIZE) // 2),
    *BALL_SIZE
)



#! Game loop

clock = pg.time.Clock()
dt = 0

running = True
while running:
    # Quit game
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False

    for p in [player1, player2]:
        p.update(dt)

    # Player2 AI:
    #! player2.centery = ball.centery

    # Move ball
    ball.x += ball_speed[0] * dt
    ball.y += ball_speed[1] * dt

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] *= -1

    if ball.left <= 0 or ball.right >= WIDTH:
        ball.center = CENTER
        ball_speed[0] *= -1

    if ball.colliderect(player1.rect) or ball.colliderect(player2.rect):
        ball_speed[0] *= -1

    # Drawing
    screen.fill(BLACK)
    for p in [player1, player2]:
        pg.draw.rect(screen, WHITE, p.rect)

    pg.draw.ellipse(screen, WHITE, ball)
    pg.draw.aaline(screen, WHITE, (CENTER[0], 0), (CENTER[0], HEIGHT))

    pg.display.flip()
    dt = clock.tick(144) / 10


pg.quit()