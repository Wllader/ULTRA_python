from matplotlib import pyplot as plt
import numpy as np, cv2 as cv

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