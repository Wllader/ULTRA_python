import cv2 as cv, numpy as np
from matplotlib import pyplot as plt

# Kód pro pohodlné prezentování obrázků:
def show(*images, scale=1, cols=2, titles=None):
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
            ax.imshow(img_rgb)
            if titles and i < len(titles):
                ax.set_title(titles[i], fontsize=8)
    
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0.01, hspace=0.01)
    plt.show()



# img = np.zeros((300, 300, 3), dtype=np.uint8)
# img[:] = (163, 163, 163)

# img2 = np.random.random((300, 300, 3)) * 255

# show(img, img2, cols=2)


# img = np.zeros((400, 400, 3), dtype=np.uint8)
# tmp = img.copy()

# cv.rectangle(tmp, (50, 50), (350, 150), (255, 0, 0), thickness=3)
# img |= tmp
# tmp[:] = (0, 0, 0)

# cv.circle(tmp, (200, 150), 50, (0, 255, 0), thickness=-1)
# img |= tmp
# tmp[:] = (0, 0, 0)

# cv.line(tmp, (0, 0), (400, 400), (0, 0, 255), thickness=2)
# img |= tmp
# tmp[:] = (0, 0, 0)

# show(img, scale=1)


img = cv.imread("lena.tif")
if img is None:
    print("None")
    exit()

img_gs = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print(img.shape, img_gs.shape)

# show(img, img_gs, cols=2)

def roberts(img, thresh):
    mask = np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]])

    g1 = cv.filter2D(img, ddepth=-1, kernel=mask)
    g2 = cv.filter2D(img, ddepth=-1, kernel=np.rot90(mask))
    g3 = cv.filter2D(img, ddepth=-1, kernel=np.rot90(mask, 2))
    g4 = cv.filter2D(img, ddepth=-1, kernel=np.rot90(mask, 3))


    edges1 = np.hypot(g1, g2) >= thresh
    edges2 = np.hypot(g3, g4) >= thresh

    edges = edges1 | edges2

    return edges.astype(np.uint8) * 255


show(img_gs, roberts(img_gs, 250), cols=2)