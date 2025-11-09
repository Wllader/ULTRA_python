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
canvas_show = Canvas(screen, (300, 50), (280, 280)).disable()

barplot_adr = BarPlot(screen, (10, 370), (300, 280), data, labels, fg=(100, 220, 100))
barplot_csr = BarPlot(screen, (320, 370), (300, 280), data, labels, fg=(100, 220, 100))
barplot_mlr = BarPlot(screen, (630, 370), (300, 280), data, labels, fg=(100, 220, 100))
barplot_mlp = BarPlot(screen, (940, 370), (300, 280), data, labels, fg=(100, 220, 100))


btn_clear = Button(screen, (10, 10), (100, 30), "Clear", command=canvas.clear)
btn_random = Button(screen, (120, 10), (100, 30), "Random",
                    command=lambda: canvas.from_array(X_test[np.random.randint(0, X_test.shape[0])]))

chbx_centerd = CheckBox(screen, (230, 10), (30, 30))

g_widgets = pg.sprite.Group(
    canvas, canvas_show,
    barplot_adr, barplot_csr, barplot_mlr, barplot_mlp,
    btn_clear, btn_random, chbx_centerd
)

adr = AverageDistanceRecognizer(X_train, y_train)
csr = CosineSimilarityRecognizer(X_train, y_train)
mlr = MulticlassLogisticRegression(X_train, y_train)
mlp = MultilayerPerceptronRecognizer(
    X_train,
    y_train,
    (16, 16),
    batch_size=8
)

#! Game loop
while gc.running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gc.stop()
        else:
            #Update 
            g_widgets.update(event)

    canvas_show.from_array(
        canvas.get_centered_image() if chbx_centerd.get() else canvas.get_array()
    )

    barplot_adr.set_data(adr.predict(canvas_show.get_array()))
    barplot_csr.set_data(csr.predict(canvas_show.get_array()))
    barplot_mlr.set_data(mlr.predict(canvas_show.get_array()))
    barplot_mlp.set_data(mlp.predict(canvas_show.get_array()))

    #Draw
    screen.fill(GREY * 56)
    g_widgets.draw(screen)


    pg.display.flip()
    gc.tick(144)

pg.quit()