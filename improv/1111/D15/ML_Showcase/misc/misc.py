from enum import Enum, auto

class FileType(Enum):
    TrainImage = auto()
    TrainLabel = auto()
    TestImage = auto()
    TestLabel = auto()


def download():
    import urllib.request
    import os

    data_folder = os.path.join(os.getcwd(), 'data')
    os.makedirs(data_folder, exist_ok=False)

    urllib.request.urlretrieve('https://azureopendatastorage.blob.core.windows.net/mnist/train-images-idx3-ubyte.gz',
                            filename=os.path.join(data_folder, 'train-images.gz'))
    urllib.request.urlretrieve('https://azureopendatastorage.blob.core.windows.net/mnist/train-labels-idx1-ubyte.gz',
                            filename=os.path.join(data_folder, 'train-labels.gz'))
    urllib.request.urlretrieve('https://azureopendatastorage.blob.core.windows.net/mnist/t10k-images-idx3-ubyte.gz',
                            filename=os.path.join(data_folder, 'test-images.gz'))
    urllib.request.urlretrieve('https://azureopendatastorage.blob.core.windows.net/mnist/t10k-labels-idx1-ubyte.gz',
                            filename=os.path.join(data_folder, 'test-labels.gz'))
    


# load compressed MNIST gz files and return numpy arrays
def load_data(filename, label=False):
    import gzip
    import numpy as np
    import struct

    with gzip.open(filename) as gz:
        struct.unpack('I', gz.read(4))
        n_items = struct.unpack('>I', gz.read(4))
        if not label:
            n_rows = struct.unpack('>I', gz.read(4))[0]
            n_cols = struct.unpack('>I', gz.read(4))[0]
            res = np.frombuffer(gz.read(n_items[0] * n_rows * n_cols), dtype=np.uint8)
            res = res.reshape(n_items[0], n_rows * n_cols)
        else:
            res = np.frombuffer(gz.read(n_items[0]), dtype=np.uint8)
            res = res.reshape(n_items[0], 1)
    return res


def get_data(ft:FileType, reshape:bool=True):
    data = target = None

    match ft:
        case FileType.TrainImage:
            data = load_data("data/train-images.gz", False)

        case FileType.TestImage:
            data = load_data("data/test-images.gz", False)

        case FileType.TrainLabel:
            target = load_data("data/train-labels.gz", True)

        case FileType.TestLabel:
            target = load_data("data/test-labels.gz", True)


    if data is not None:
        return data.reshape((data.shape[0], 28, 28)) if reshape else data

    if target is not None:
        return target.flatten() if reshape else target








# Kód pro pohodlné prezentování obrázků:
def show(*images, scale=1, cols=2, titles=None, returned=False):
    import cv2 as cv, numpy as np
    from matplotlib import pyplot as plt

    n_images = len(images)
    if n_images == 1: cols = 1
    rows = (n_images + cols - 1) // cols

    # Assume all images are roughly same size (or take the first as reference)
    height, width = images[0].shape[:2]
    
    # Set figure size to match the total pixel size exactly
    dpi = 100
    fig_width = (width * cols) / (dpi / scale)
    fig_height = (height * rows) / (dpi / scale)

    fig, axes = plt.subplots(rows, cols, figsize=(fig_width, fig_height))
    axes = np.array(axes).reshape(-1)  # Flatten in case it's 2D array

    fig.patch.set_facecolor('none')

    for i, ax in enumerate(axes):
        ax.set_facecolor('none')
        ax.axis('off')

        if i < n_images:
            img_rgb = cv.cvtColor(images[i].astype(np.uint8), cv.COLOR_BGR2RGB)
            img_rgb = cv.resize(img_rgb, (int(width*scale), int(height*scale)), interpolation=cv.INTER_NEAREST)
            ax.imshow(img_rgb, cmap="gray")
            if titles and i < len(titles):
                ax.set_title(titles[i], fontsize=8)
    
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0.05, wspace=0.01, hspace=0.01)
    if not returned:
        plt.show()
    else:
        return fig, axes
    
if __name__ == "__main__":
    download()