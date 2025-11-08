import pygame as pg, numpy as np
from misc.widgets import *
from misc.game_controller import GameController
from misc.recognizers import *
from misc.misc import get_data, FileType


pg.init()
screen = pg.display.set_mode((1900, 1000))
gc = GameController()


labels = [f"{i}" for i in range(10)]
data = np.zeros(10)
X_test = get_data(FileType.TestImage)
X_train=get_data(FileType.TrainImage)
y_train=get_data(FileType.TrainLabel)

canvas = Canvas(screen, (10, 50), (280, 280))
canvas_show = Canvas(screen, (300, 50), (280, 280))
canvas_show.disable()

btn_clear = Button(screen, (10, 10), (100, 30), "Clear", command=canvas.clear)
btn_random = Button(screen, (120, 10), (100, 30), "Randomize", 
                    command=lambda: canvas.from_array(X_test[np.random.randint(0, X_test.shape[0])]))
chbx_center = CheckBox(screen, (230, 10), (30, 30))

barplot_adr = BarPlot(screen, (10, 370), (300, 280), data, labels, fg=(100, 220, 100))
barplot_csr = BarPlot(screen, (320, 370), (300, 280), data, labels, fg=(100, 220, 100))

barplot_mlr = BarPlot(screen, (630, 370), (300, 280), data, labels, fg=(100, 220, 100))
canvas_mlr_weights = Canvas(screen, (630, 670), (300, 300))
canvas_mlr_weights.disable()

barplot_mlp = BarPlot(screen, (940, 370), (300, 280), data, labels, fg=(100, 220, 100))
# canvas_mlp_weights = Canvas(screen, (940, 670), (300, 300))
# canvas_mlp_weights.disable()


g_widgets = pg.sprite.Group(
    canvas, canvas_show, canvas_mlr_weights,
    btn_clear, btn_random,
    chbx_center,
    barplot_adr, barplot_csr, barplot_mlr, barplot_mlp
)

adr = AverageDistanceRecognizer(
    X_train,
    y_train,
    normalize=True
)

csr = CosineSimilarityRecognizer(
    X_train,
    y_train,
    normalize=True
)

mlr = MulticlassLogisticRegressionRecognizer(
    X_train,
    y_train,
)

mlp = MultilayerPerceptronRecognizer(
    X_train,
    y_train,
    (16, 16),
    batch_size=8
)

while gc.running:
    event = None
    for e in pg.event.get():
        if e.type == pg.QUIT:
            gc.stop()
        else:
            event = e

    #Update
    g_widgets.update(e)

    canvas_show.from_array(
        canvas.get_centered_image() if chbx_center.get() else canvas.get_array()
    )

    barplot_adr.set_data(adr.predict(canvas_show.get_array()))
    barplot_csr.set_data(csr.predict(canvas_show.get_array()))
    barplot_mlr.set_data(mlr.predict(canvas_show.get_array()))
    barplot_mlp.set_data(mlp.predict(canvas_show.get_array()))

    canvas_mlr_weights.from_array(
        mlr.weights.mean(axis=1)[:-1].reshape((28, 28)),
        normalize=True
    )

    #Draw
    g_widgets.draw(screen)

    #Refresh
    pg.display.flip()
    gc.tick(144)

pg.quit()
