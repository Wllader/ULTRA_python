import pygame as pg, numpy as np

pg.init()

#Constants
SIZE = W, H = np.array([800, 600])
CENTER = SIZE / 2

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

PADDLE_DIMS = PW, PH = np.array([10, 100])
PADDLE_SPEED = np.array([0, 5])

BALL_SIZE = np.array([16, 16])
BALL_SPEED = np.array([5, 5])


#Objects
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Pong!")
clock = pg.time.Clock()




#! Game Loop
running = True
dt = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #Update


    #Draw
    screen.fill(GREY * 28)


    pg.display.flip()
    dt = clock.tick(144) / 10


pg.quit()