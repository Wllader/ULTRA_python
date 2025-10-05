import pygame as pg, numpy as np
from widgets import Button, Entry
from game_controller import GameController
from plot import Plot
import logging, requests, pandas as pd

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

pg.init()
SIZE = W, H = np.array([800, 600])
screen = pg.display.set_mode(SIZE)
logger = logging.getLogger(__name__)

plot = Plot(screen, (0, 60), (W, H-70))
def plot_function(tick, days, gran=50):
    if tick == "random":
        d = np.linspace(-5, 5, days*100)
        plot.set_data(np.sin(d*(days/100) + np.random.rand(1) * 2*np.pi), gran)
        plot.move_particles()
        return
    
    logger.info("Fetching!")
    response = requests.get(f"http://localhost:8000/coin/{tick}?{days=}")
    d = response.json()
    if "Price" in d:
        logger.info("Passed!")
        d = pd.DataFrame(d)

        plot.set_data(d["Price"].to_numpy(float), gran)
        plot.move_particles()

    else:
        logger.warning(f"Failed: {tick}")


e_tick = Entry(screen, (10, 10), (150, 40), default_text="random", tooltip_text="Coin tick")
e_days = Entry(screen, (170, 10), (70, 40), default_text="5", tooltip_text="#Days")
e_gran = Entry(screen, (250, 10), (100, 40), default_text="50", tooltip_text="Granularity")



g_entries = pg.sprite.Group(
    e_tick,
    e_days,
    e_gran
)

g_widgets = pg.sprite.Group(
    g_entries,
    Button(screen, (360, 10), (150, 40), text="Click me!", command=lambda: plot_function(e_tick.text, int(e_days.text), int(e_gran.text))),
    plot
)

#! Game loop
gc = GameController()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        else:
            #Update
            g_widgets.update(event)


    #Draw
    screen.fill(GREY * 56)
    g_widgets.draw(screen)

    pg.display.flip()
    gc.tick(144)

pg.quit()