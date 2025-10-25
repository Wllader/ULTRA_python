import pygame as pg, numpy as np
from pong_entities import PongPlayer, PongBall, PongBot, PongBotAdvanced
from game_controller import GameController
from spritesheet_sr_fc import SpriteSheet

pg.init()

#Constants
SIZE = W, H = np.array([800, 600])
CENTER = SIZE // 2

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

PADDLE_DIMS = PW, PH = np.array([10, 100])
PADDLE_SPEED = np.array([0, 5])

BALL_SIZE = np.array([16, 16])
BALL_SPEED = np.array([5, 7])


#Object
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Pong!")
gc = GameController()

bg = pg.image.load("Sprites/Bg.png")
bg = pg.transform.scale_by(bg, W / bg.get_width())

player1 = PongBotAdvanced(
    screen,
    PADDLE_DIMS,
    (55, CENTER[1]),
    PADDLE_SPEED,
    (0, 255, 0),
    SpriteSheet(
        "Sprites/Paddle.png",
        (5, 50),
        2
    )
)

bot = PongBotAdvanced(
    screen,
    PADDLE_DIMS,
    (W-55, CENTER[1]),
    PADDLE_SPEED,
    (255, 0, 0),
    SpriteSheet(
        "Sprites/Paddle.png",
        (5, 50),
        2,
        1
    )
)

ball = PongBall(
    screen,
    BALL_SIZE,
    CENTER,
    BALL_SPEED,
    WHITE,
    SpriteSheet(
        "Sprites/Ball.png",
        (16, 16)
    )
)

ball.g_bounce.add(player1, bot)
bot.ball = ball
player1.ball = ball




g_entites = pg.sprite.Group(
    player1, bot, ball
)


#! Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    # Update
    g_entites.update()


    # Draw
    screen.fill(GREY * 28)
    screen.blit(bg, (0, 0))
    g_entites.draw(screen)


    # Tick
    pg.display.flip()
    gc.tick(144, 10)

pg.quit()


#Todo Postavit základní PyGame skript
#? (Inicializace, definice konstant, definice objektů, game loop (Event management, Update, Draw, Tick))

#Todo Přidat objekty z pong_entities.py a zprovoznit je pro jednoduchou hru Pong
# Pokud to nepůjde, nic se neděje!