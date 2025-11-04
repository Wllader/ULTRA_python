from misc.misc import get_data, FileType, show
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec


# One item in X_train is 784 (28^2) values 0-255 (greyscale)
#  representing numbers 0-9 written in a 28x28px box
X_train = get_data(FileType.TrainImage)
y_train = get_data(FileType.TrainLabel)

X_test = get_data(FileType.TestImage)
y_test = get_data(FileType.TestLabel)


pictures = [ X_train[(y_train == n).flatten()] for n in range(10) ]
averages = np.array([ pictures[i].mean(axis=0) for i in range(10) ])


while True:
    T = np.random.randint(0, 10000)
    output = (averages * X_test[T]).sum(axis=(1, 2))

    fig, axes = show(*averages, X_test[T], averages[output.argmax()], cols=len(averages), returned=True)
    gs = gridspec.GridSpec((rows := int(np.ceil(len(axes) / (cols := len(averages))))) + 1, cols, fig, height_ratios=rows * [1] + [3])
    for i, ax in enumerate(axes):
        r, c = divmod(i, len(averages))
        ax.set_subplotspec(gs[r, c])


    ax_bar = fig.add_subplot(gs[-1, :])
    colors = plt.cm.RdYlGn((output / output.max())**2)
    edgecolors = [ "none" if n != output.argmax() else "red" for n in range(10) ]
    edgecolors[y_test[T]] = "blue"
    ax_bar.bar([ str(n) for n in range(10)], output, color=colors, edgecolor=edgecolors)
    fig.set_size_inches(6, 5)
    plt.show()