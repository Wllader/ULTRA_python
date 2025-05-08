import numpy as np, cv2 as cv
from helper_funcs import show

def checkerboard(w, h, px):
    tile = np.array([[0, 255],[255, 0]], dtype=np.uint8)
    img = np.tile(tile, (h // 2 + h % 2, w // 2 + w % 2))[:h, :w]
    img = cv.resize(img, np.array([w, h]) * px, interpolation=cv.INTER_NEAREST)

    return img

c = checkerboard(5, 8, 20)

def bayer(w, h, px):
    #~ tile = np.zeros((2, 2, 3), dtype=np.uint8)
    r = np.array([[0, 255], [0, 0]], dtype=np.uint8)
    g = np.array([[255, 0], [0, 255]], dtype=np.uint8)
    b = np.array([[0, 0], [255, 0]], dtype=np.uint8)

    r = np.tile(r, (h // 2 + h % 2, w // 2 + w % 2))[:h, :w]
    g = np.tile(g, (h // 2 + h % 2, w // 2 + w % 2))[:h, :w]
    b = np.tile(b, (h // 2 + h % 2, w // 2 + w % 2))[:h, :w]

    img = np.stack((b, g, r), -1)
    img = cv.resize(img, np.array([w, h]) * px, interpolation=cv.INTER_NEAREST)
    
    return img
    


b = bayer(5, 8, 20)
show(c, b)