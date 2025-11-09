import pygame as pg, numpy as np
from misc.game_controller import GameController
import logging
from misc.widgets import *
from misc.misc import get_data, FileType
from misc.recognizers import *

logging.basicConfig(level=logging.INFO)


pg.init()
SIZE = W, H = np.array([1900, 1000])
screen = pg.display.set_mode(SIZE)
gc = GameController()

labels = [f"{i}" for i in range(10)]
data = np.zeros(10)

X_test = get_data(FileType.TestImage)
X_train = get_data(FileType.TrainImage)
y_train = get_data(FileType.TrainLabel)

canvas = Canvas(screen, (10, 50), (280, 280))

barplot_adr = BarPlot(screen, (10, 370), (300, 280), data, labels, fg=(100, 220, 100))
barplot_csr = BarPlot(screen, (320, 370), (300, 280), data, labels, fg=(100, 220, 100))
barplot_mlr = BarPlot(screen, (630, 370), (300, 280), data, labels, fg=(100, 220, 100))


btn_clear = Button(screen, (10, 10), (100, 30), "Clear", command=canvas.clear)

g_widgets = pg.sprite.Group(
    canvas,
    barplot_adr, barplot_csr, barplot_mlr,
    btn_clear
)

adr = AverageDistanceRecognizer(X_train, y_train)
csr = CosineSimilarityRecognizer(X_train, y_train)
mlr = MulticlassLogisticRegression(X_train, y_train)

#! Game loop
while gc.running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gc.stop()
        else:
            #Update 
            g_widgets.update(event)
            
    barplot_adr.set_data(adr.predict(canvas.get_array()))
    barplot_csr.set_data(csr.predict(canvas.get_array()))
    barplot_mlr.set_data(mlr.predict(canvas.get_array()))

    #Draw
    screen.fill(GREY * 56)
    g_widgets.draw(screen)


    pg.display.flip()
    gc.tick(144)

pg.quit()