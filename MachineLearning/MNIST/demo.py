import pygame as pg, numpy as np
from misc.widgets import Canvas, Button, Label, BarPlot
from misc.game_controller import GameController
from misc.recognizers import AverageDistanceRecognizer, CosineSimilarityRecognizer
from misc.misc import get_data, FileType


pg.init()
screen = pg.display.set_mode((800, 800))
gc = GameController()


labels = [f"{i}" for i in range(10)]
data = np.zeros(10)
X_test = get_data(FileType.TestImage)
X_train=get_data(FileType.TrainImage)
y_train=get_data(FileType.TrainLabel)

canvas = Canvas(screen, (10, 50), (280, 280))
barplot_adr = BarPlot(screen, (300, 50), (300, 280), data, labels, fg=(100, 220, 100))
barplot_csr = BarPlot(screen, (300, 370), (300, 280), data, labels, fg=(100, 220, 100))
btn_clear = Button(screen, (10, 10), (100, 30), "Clear", command=canvas.clear)
btn_random = Button(screen, (120, 10), (100, 30), "Randomize", 
                    command=lambda: canvas.set_array(X_test[np.random.randint(0, X_test.shape[0])]))

g_widgets = pg.sprite.Group(
    canvas, btn_clear, btn_random, barplot_adr, barplot_csr
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

while gc.running:
    event = None
    for e in pg.event.get():
        if e.type == pg.QUIT:
            gc.stop()
        else:
            event = e

    #Update
    g_widgets.update(e)
    barplot_adr.set_data(adr.predict(canvas.get_array()))
    barplot_csr.set_data(csr.predict(canvas.get_array()))

    #Draw
    g_widgets.draw(screen)

    #Refresh
    pg.display.flip()
    gc.tick(144)

pg.quit()
