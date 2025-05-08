import pygame as pg, numpy as np

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
BALL_SIZE = np.array([15, 15])

# Positions
player1 = pg.Rect(
    50, 
    CENTER[1],
    *PADDLE_DIMS
)

player2 = pg.Rect(
    WIDTH - 50 - PW, 
    CENTER[1],
    *PADDLE_DIMS
)

ball = pg.Rect(
    *((SIZE - BALL_SIZE) // 2),
    *BALL_SIZE
)

# Speeds
paddle_speed = 7
ball_speed = np.array([0, 5])

#! Game loop

clock = pg.time.Clock()
dt = 0

running = True
while running:
    # Quit game
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False
    
    # Key input
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player1.y -= paddle_speed * dt
    if keys[pg.K_s]:
        player1.y += paddle_speed * dt

    # Player2 AI:
    player2.centery = ball.centery
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= HEIGHT:
        player2.bottom = HEIGHT

    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= HEIGHT:
        player1.bottom = HEIGHT

    # Move ball
    ball.x += ball_speed[0] * dt
    ball.y += ball_speed[1] * dt

    # Collisions:
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] *= -1

    if ball.left <= 0 or ball.right >= WIDTH:
        ball.center = CENTER
        ball_speed[0] *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] *= -1

    # Drawing
    screen.fill(BLACK)
    for p in [player1, player2]:
        pg.draw.rect(screen, WHITE, p)

    pg.draw.ellipse(screen, WHITE, ball)
    pg.draw.aaline(screen, WHITE, (CENTER[0], 0), (CENTER[0], HEIGHT))

    pg.display.flip()
    dt = clock.tick(60) / 10


pg.quit()