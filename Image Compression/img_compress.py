import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.cluster import MiniBatchKMeans
from tkinter.filedialog import Tk
from tkinter.filedialog import askopenfilename


if __name__ == '__main__':
    image_formats = ['tif', 'jpg', 'gif', 'png']

    # The script takes as a parameter the number of desired colors for the new image
    if len(sys.argv) < 2:
        print("No number of colors specified.\nRe-run the script specifying the number of"\
        " desired colors.")
        sys.exit(1)

    # Get pic path and number of colors
    Tk().withdraw()
    pic_path = askopenfilename()

    if (len(pic_path) < 1) | (pic_path.split("/")[-1].split(".")[1] not in image_formats):
        print("No image selected. You can select: ", image_formats, "formats")
        sys.exit(1)

    # Measure runtime
    start_time = time.time()
    n_colors = int(sys.argv[1])

    # Reads the image in BGR format
    img = cv2.imread(pic_path)
    # BGR->RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Normalize the colors so that they are between 0&1 and reshape the data for a typical
    # scikit-learn input
    X = (img/255.0).reshape(-1, 3)

    # KMeans model
    model = MiniBatchKMeans(n_clusters=n_colors)
    classf = model.fit_predict(X)

    # The new colors are the centers of the clusters
    # Basically we create a new image where the true input color is replaced by the color of
    # the closest cluster
    new_colors = model.cluster_centers_
    new_image = new_colors[classf].reshape(img.shape)
    new_image = (new_image*255).astype(np.uint8)

    # Save the new image
    plot = plt.imshow(new_image)

    # Remove axes and whitespaces sorrounding the image
    plt.axis('off')
    plt.savefig("compressed_"+pic_path.split("/")[-1], bbox_inches=0)
    print("Runtime:::: {0} seconds".format(round((time.time()-start_time), 2)))