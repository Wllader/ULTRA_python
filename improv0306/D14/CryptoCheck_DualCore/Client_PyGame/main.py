import pygame as pg, numpy as np, pandas as pd
import requests
from widgets import *
from plot import Plot



pg.init()
SIZE = W, H = np.array([1000, 600])
screen = pg.display.set_mode(SIZE)

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0

plot = Plot(screen, np.array((0, 60)), np.array((W, H-60)))
def plot_function(tick, days, gran=50):
    days = int(days)
    gran = int(gran)

    if tick == "random":
        d = np.linspace(-5, 5, days*100)
        plot.set_data(np.sin(d + np.random.rand(1) * 2*np.pi), gran)
        plot.move_particles()
        return
    
    print("Fetching!")
    response = requests.get(f"http://localhost:8000/coin/{tick}?{days=}")
    d = response.json()
    if "Price" in d:
        print("Passed")
        d = pd.DataFrame(d)

        plot.set_data(d["Price"].to_numpy(float), gran)
        plot.move_particles()

    else:
        print("Failed:", tick)


e_tick = Entry(screen, np.array([10, 10]), np.array([150, 40]), default_text="random", tooltip_text="Coin tick")
e_days = Entry(screen, np.array([170, 10]), np.array([70, 40]), default_text="5", tooltip_text="#Days")
e_gran = Entry(screen, np.array([250, 10]), np.array([100, 40]), default_text="50", tooltip_text="Granularity")


entries = pg.sprite.Group(
    e_tick,
    e_days,
    e_gran
)

widgets = pg.sprite.Group(
   entries,
   Button(screen, np.array([360, 10]), np.array([150, 40]), "Click me!", command=lambda: plot_function(e_tick.text, e_days.text, e_gran.text)),
   plot
)


#! Game loop
running = True
clock = pg.time.Clock()
while running:
    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        else:
            # Update
            widgets.update(event)

    #Draw
    screen.fill(GREY * 56)
    widgets.draw(screen)


    pg.display.flip()
    clock.tick(144)

pg.quit()