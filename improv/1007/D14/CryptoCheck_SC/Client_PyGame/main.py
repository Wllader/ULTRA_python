import pygame as pg, numpy as np
from game_controller import GameController
import logging, requests, pandas as pd
from plot import Plot

from widgets import *

logging.basicConfig(level=logging.INFO)


GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

pg.init()
SIZE = W, H = np.array([800, 600])
screen = pg.display.set_mode(SIZE)
logger = logging.getLogger(__name__)
gc = GameController()

plot = Plot(screen, (10, 60), (W-20, H-70))
def plot_function(tick, days, gran=50):
    if tick == "random":
        d = np.linspace(-5, 5, days*150)
        plot.set_data(np.sin(d*(days/100) + np.random.rand(1) * 2*np.pi), gran)
        plot.move_particles()
        return
    
    logger.info("Fetching!")
    response = requests.get(f"http://localhost:8000/coin/{tick}?{days=}")
    d = response.json()
    if "Price" in d:
        logger.info("Passed")
        d = pd.DataFrame(d)

        plot.set_data(d["Price"].to_numpy(float), gran)
        plot.move_particles()
    
    else:
        logger.warning(f"Failed: {tick}")



e_tick = Entry(screen, (10, 10), (150, 40), default_text="random", tooltip_text="Coint tick")
e_days = Entry(screen, (170, 10), (70, 40), default_text="5", tooltip_text="#Days")
e_gran = Entry(screen, (250, 10), (100, 40), default_text="50", tooltip_text="Granularity")

g_entries = pg.sprite.Group(
    e_tick, e_days, e_gran
)


g_widgets = pg.sprite.Group(
    Button(screen, (360, 10), (150, 40), text="Click me!", command=lambda: plot_function(
        e_tick.text, int(e_days.text), int(e_gran.text)
    )),
    g_entries,
    plot
)


#! Game loop
while gc.running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gc.stop()
        else:
            #Update 
            g_widgets.update(event)
            

    #Draw
    screen.fill(GREY * 56)
    g_widgets.draw(screen)


    pg.display.flip()
    gc.tick(144)

pg.quit()