import pygame as pg, numpy as np
from pong_entities import PongPlayer, PongBot, PongBall
from game_controller import GameController



pg.init()

# Constants
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
gc = GameController()

bg = pg.image.load("Sprites/Bg.png").convert()
bg = pg.transform.scale_by(bg, W / bg.width)

player = PongBot(
    screen,
    PADDLE_DIMS,
    (50, CENTER[1]),
    PADDLE_SPEED,
    (0, 255, 0)
)

bot = PongBot(
    screen,
    PADDLE_DIMS,
    (W-50, CENTER[1]),
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

bot.ball = ball
player.ball = ball


g_paddles = pg.sprite.Group(
    player, bot
)

ball.g_bounce.add(g_paddles)


g_entities = pg.sprite.Group(
    g_paddles, ball
)


#! Game loopw
while gc.running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gc.stop()

    
    #Update
    g_entities.update()

    #Draw
    screen.fill(GREY * 28)
    screen.blit(bg, (0, 0))
    g_entities.draw(screen)



    pg.display.flip()
    gc.tick(144, 10)


pg.quit()