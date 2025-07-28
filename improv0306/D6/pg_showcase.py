# Import a základní inicializace
import pygame as pg, numpy as np
from square import Square, Moving_Square
from game_controller import GameController

pg.init()

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

# Inicializace objektů
SIZE = W, H = np.array([800, 600])
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("My first game")
gc = GameController()

player = Square(
    screen, 
    np.array([200, 200]), 
    np.array([50, 50])
)

p2 = Moving_Square(
    screen,
    np.array([400, 200]),
    np.array([50, 50]),
    GREY*160,
    np.array([7, 5])
)
p2.collission_group.add(player)
player.collission_group.add(p2)


players = pg.sprite.Group(
    player, p2
)

#~ p = pg.Rect(50, 50, 50, 50)


#! Game loop
running = True
while running:
    # Event-management
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    # Update
    players.update()


    # Vykreslování (Draw)
    screen.fill(GREY * 28)

    #~ pg.draw.rect(screen, BLACK, p)
    #~ screen.blit(player.image, player.rect)
    players.draw(screen)

    pg.display.flip()
    gc.tick(144, 10)


pg.quit()