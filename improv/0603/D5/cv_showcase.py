from matplotlib import pyplot as plt
import numpy as np, cv2 as cv
from helper_functions import show


# img = np.zeros((400, 400, 3), dtype=np.uint8)
# tmp = np.zeros((400, 400, 3), dtype=np.uint8)


# cv.rectangle(tmp, (50, 50), (350, 150), (255, 0, 0), thickness=3)
# img = tmp | img
# tmp[:] = (0, 0, 0)

# cv.circle(tmp, (200, 150), 60, (0, 255, 0), thickness=-1)
# img |= tmp
# tmp[:] = (0, 0, 0)

# cv.line(tmp, (0, 0), (400, 400), (0, 0, 255), thickness=2)
# img |= tmp
# tmp[:] = (0, 0, 0)

# show(img)

img = cv.imread("images/lena_color_512.tif")
if img is None:
    print("None")
    exit()

img_gs = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


def kirsch(img, thresh):
    mask_cardinal = -np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    mask_diagonal = -np.array([[0, -1, -1], [1, 0, -1], [1, 1, 0]])

    g1 = cv.filter2D(img, ddepth=-1, kernel=mask_diagonal)
    g2 = cv.filter2D(img, ddepth=-1, kernel=np.rot90(mask_diagonal))

    g3 = cv.filter2D(img, ddepth=-1, kernel=mask_cardinal)
    g4 = cv.filter2D(img, ddepth=-1, kernel=mask_cardinal.T)

    edges1 = np.hypot(g1, g2) >= thresh
    edges2 = np.hypot(g3, g4) >= thresh

    edges = edges1 | edges2

    return edges.astype(np.uint8) * 255



# e = kirsch(img_gs, 60)
# show(img_gs, e)


plt.hist(img_gs.flatten(), 50)
plt.grid()
plt.show()


