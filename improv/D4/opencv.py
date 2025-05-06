import cv2 as cv, numpy as np
from matplotlib import pyplot as plt

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

img = np.zeros((300, 300, 3), dtype=np.uint8)
# img1 = np.zeros((300, 300, 3), dtype=np.uint8)
# img2 = np.zeros((300, 300, 3), dtype=np.uint8)
# img3 = np.zeros((300, 300, 3), dtype=np.uint8)
# # img[:] = (255, 0, 0)

# # img_random = np.random.random((300, 300, 3)) * 255

# # show(img, img_random)

# cv.rectangle(img1, (50, 50), (150, 200), (255, 0, 0), thickness=3)
# cv.circle(img2, (200, 150), 50, (0, 128, 128), thickness=-1)
# cv.line(img3, (0, 0), (300, 300), (0, 0, 255), thickness=2)


# show(img1 | img2 | img3)

img = cv.imread("soubory/lena_color_512.tif")
if img is None:
    print("None")
    exit()

img_gs = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# print(img.shape, img_gs.shape)

# show(img, img_gs)

def roberts(img, thresh, basic=False):
    mask_diagonal = np.array([[0, 1], [-1, 0]])
    mask_cardinal = np.array([[-1, 1]])

    g1 = cv.filter2D(img, ddepth=-1, kernel=mask_diagonal)
    g2 = cv.filter2D(img, ddepth=-1, kernel=np.rot90(mask_diagonal))

    g3 = cv.filter2D(img, ddepth=-1, kernel=mask_cardinal)
    g4 = cv.filter2D(img, ddepth=-1, kernel=mask_cardinal.T)

    edges1 = np.hypot(g1, g2) >= thresh
    edges2 = np.hypot(g3, g4) >= thresh

    edges = edges1 if basic else (edges1 | edges2)
    return edges.astype(np.uint8) * 255

def prewitt(img, thresh):
    mask_cardinal = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    mask_diagonal = np.array([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])

    g1 = cv.filter2D(img, ddepth=-1, kernel=mask_diagonal)
    g2 = cv.filter2D(img, ddepth=-1, kernel=np.rot90(mask_diagonal))

    g3 = cv.filter2D(img, ddepth=-1, kernel=mask_cardinal)
    g4 = cv.filter2D(img, ddepth=-1, kernel=np.rot90(mask_cardinal))

    edges1 = np.hypot(g1, g2) >= thresh
    edges2 = np.hypot(g3, g4) >= thresh

    edges = edges1 | edges2
    return edges.astype(np.uint8) * 255

# show(
#     roberts(img_gs, 20), roberts(img_gs, 20, True),
#     prewitt(img_gs, 60), img_gs
# )

def checkerboard(w, h, px):
    tile = np.array([[0, 255],[255, 0]], dtype=np.uint8)
    img = np.tile(tile, (h // 2 + h % 2, w // 2 + w % 2))[:h, :w]
    img = cv.resize(img, np.array([w, h]) * px, interpolation=cv.INTER_NEAREST)

    return img

def checkerboard2(w, h, px):
    img = np.zeros((h, w), dtype=np.uint8)
    img[::2, ::2] = 255
    img[1::2,1::2] = 255
    img = cv.resize(img, np.array([w, h]) * px, interpolation=cv.INTER_NEAREST)

    return img

def checkerboard3(w, h, px):
    black = np.zeros((px, px), dtype=np.uint8)
    white = np.ones((px, px), dtype=np.uint8) * 255

    r1 = np.hstack((black, white))
    r2 = np.hstack((white, black))

    tile = np.vstack((r1, r2))

    img = np.tile(tile, (h, w)) # Wrong height and width calculation
    return img

show(checkerboard3(5, 3, 20))