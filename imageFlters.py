import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
# This import statement is used to import the python packages or
# modules that required by our program.
# Here we are importing cv2 module which is used for image
# reading and also for displaying images.
# opencv read the images a numpy arrays.
# Here also we are importing matplotlib.pyplot
# Here we are also importing matplotlib.pyplot
# which provides an implicit, MATLAB-like, way of plotting.
# It also used to opens figures on your screen,
# and also acts as the figure GUI manager.
# Pyplot module is mainly intended for
# interactive plots and simple cases of
# programmatic plot generation.
# Here we are also importing numpy is
# used to do manipulation on array object
# Here we are also importing argparse
# which is a command-line argument
# parsing library which we are using here
# to parse path to our image files here.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--InputImage", required=False, default="imagetr.jpg", help="path to input image file to be read")
args = vars(ap.parse_args())

img = cv2.imread(args["InputImage"])
# The above function cv2.imread is used
# to read the images from the disk.

imgOrignal = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Here in the above statement we are converting our
# image from the BGR color space to the RGB
# color space.

imgGrey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# Here in the above statement we are converting our
# image from the RGB color space to the Greyscale image
# because filters can only be applied on a greyscale image.

imgBlured = cv2.GaussianBlur(imgGrey, (3, 3), 0)
# In the above statement we are applying Gaussian Blur
# to our input image. we are doing this to remove the
# noise from our image.


# The below function contains the logic for constructing
# and applying the robert filter on our input image.
def robert_filter(input_image):
    # Robert filter Kernel construction
    kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
    kernely = np.array([[0, -1], [1, 0]], dtype=int)

    # Applying the above made filter to our greyscale image
    x = cv2.filter2D(input_image, cv2.CV_16S, kernelx)
    y = cv2.filter2D(input_image, cv2.CV_16S, kernely)

    # Following statements calculates the absolute value and converts the result into 8-bit integer.
    abs_x = cv2.convertScaleAbs(x)
    abs_y = cv2.convertScaleAbs(y)

    # The below function cv2.addWeighted() calculates the weighted sum of two arrays.
    filtered_img = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    return filtered_img

# The below function contains the logic
# for constructing and applying the
# sobel filter on our input image.
def sobel_filter(input_image):
    # Sobel filter Kernel construction
    kernelx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    kernely = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)

    # Applying the above made Sobel filter to our greyscale image
    x = cv2.filter2D(input_image, cv2.CV_16S, kernelx)
    y = cv2.filter2D(input_image, cv2.CV_16S, kernely)

    # Following statements calculates the
    # absolute value and converts the
    # result into 8-bit integer.
    abs_x = cv2.convertScaleAbs(x)
    abs_y = cv2.convertScaleAbs(y)

    # The below function cv2.addWeighted()
    # calculates the weighted sum of two arrays.
    filtered_img = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    return filtered_img

# The below function contains the logic for constructing
# and applying the prewitt filter on our input image.
def prewitt_filter(input_image):
    # Sobel filter Kernel construction
    kernelx = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], np.float32)
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], np.float32)

    # Applying the above made Sobel filter to our greyscale image
    x = cv2.filter2D(input_image, cv2.CV_16S, kernelx)
    y = cv2.filter2D(input_image, cv2.CV_16S, kernely)

    # Following statements calculates the absolute value and converts the result into 8-bit integer.
    abs_x = cv2.convertScaleAbs(x)
    abs_y = cv2.convertScaleAbs(y)

    # The below function cv2.addWeighted() calculates the weighted sum of two arrays.
    filtered_img = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    return filtered_img

# The below function contains the logic for
# applying the laplacian filter on our input image.
def laplacian_filter(input_image):
    # Here in the below statement we are
    # applying laplacian filter to our image.
    # For applying Laplacian filter to our image
    # we are using cv2.Laplacian() function.
    xy = cv2.Laplacian(imgBlured, cv2.CV_16S, 3)
    abs_xy = cv2.convertScaleAbs(xy)

    # The below function cv2.addWeighted() calculates
    # the weighted sum of two arrays.
    filtered_img = abs_xy

    # In the below return statement we are
    # returning the ndarray of our filtered image.
    return filtered_img


robertFilteredImg = robert_filter(imgBlured)
sobelFilteredImg = sobel_filter(imgBlured)
laplacianFilteredImg = laplacian_filter(imgBlured)
prewittFilteredImg = prewitt_filter(imgBlured)

imagesTitle = ["Orignal Image", "Robert Filtered Image", "Sobel Filtered Image", "laplacian Filtered Image","Prewitt Filterd Image"]
imagesBoth = [imgOrignal, robertFilteredImg, sobelFilteredImg, laplacianFilteredImg, prewittFilteredImg]

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(imagesBoth[i], 'gray')
    plt.title(imagesTitle[i])

plt.show()
