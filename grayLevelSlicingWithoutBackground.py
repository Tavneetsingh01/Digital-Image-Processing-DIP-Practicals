import cv2
import numpy as np
from matplotlib import pyplot as plt
# This import statement is used to import the python packages or
# modules that required by our program.
# Here we are importing cv2 module which is used for imgOrignal
# reading and also for displaying imgOrignal in our program.
# opencv read the images a numpy arrays.
# Here also we are importing matplotlib.pyplot
# opencv read the images a numpy arrays.
# Here we are also importing matplotlib.pyplot which provides an implicit, MATLAB-like, way of plotting.
# It also used to opens figures on your screen, and also acts as the figure GUI manager.
# pyplot module is mainly intended for interactive plots and simple cases of programmatic plot generation.
# Here we are using matplotlib.pyplot to display title on our output imgOrignal.


img = cv2.imread('imagetr.jpg', 0)
# cv2.imread() function is used to read and load imgOrignal
# files stored in your system.

x, y = img.shape
z = np.zeros((x, y))
for i in range(0, x):
    for j in range(0, y):
        if 50 < img[i][j] < 150:
            z[i][j] = 255
        else:
            z[i][j] = 0
slicedImage = np.hstack((img, z))
# np.hstack() is used to concatenating the numpy arrays.

plt.title("(a) Original imgOrignal and (b) Gray level sliced imgOrignal without background")
# Here plt.title() function is used to display title on the output image plot.

plt.imshow(slicedImage, "gray")
# plt.imshow() is used to displaying the images

plt.show()
# io.show() Launch the event loop of the current gui
# plugin, and display all pending images, queued via imshow.
# A call to show will block execution of code until
# all windows have been closed.
# This io.show() is required when we are
# using imshow in non-interactive scripts.
