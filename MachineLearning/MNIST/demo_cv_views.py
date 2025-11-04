from misc.misc import get_data, FileType, show
import numpy as np
import matplotlib.pyplot as plt


# One item in X_train is 784 (28^2) values 0-255 (greyscale)
#  representing numbers 0-9 written in a 28x28px box
X_train = get_data(FileType.TrainImage)
y_train = get_data(FileType.TrainLabel)

X_test = get_data(FileType.TestImage)


pictures = [ X_train[(y_train == n).flatten()] for n in range(10) ]
averages = np.array([ pictures[i].mean(axis=0) for i in range(10) ])

plt.ion()

to_show = []
for _ in range(5):
    for n in range(10):
        rnd = np.random.randint(0, len(pictures[n]))

        to_show.append(
            pictures[n][rnd]
        )

fig, axes = show(*averages, *to_show, cols=10, returned=True)
fig.set_size_inches(6, 5)

imgs = [ ax.images[0] for ax in axes[10:] ]

while True:
    to_show = []
    for _ in range(5):
        for n in range(10):
            rnd = np.random.randint(0, len(pictures[n]))

            to_show.append(
                pictures[n][rnd]
            )

        for img, new_data in zip(imgs, to_show):
            img.set_data(new_data)

        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(.01)



    


