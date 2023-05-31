import cv2
from matplotlib import pyplot as plt
import random
import argparse
# This import statement is used to import the python packages or
# modules that required by our program.
# Here we are importing cv2 module which is used for image
# reading and also for displaying images.
# opencv read the images a numpy arrays.
# Here also we are importing matplotlib.pyplot
# opencv read the images a numpy arrays.
# Here we are also importing matplotlib.pyplot
# which provides an implicit, MATLAB-like, way of plotting.
# It also used to opens figures on your screen,
# and also acts as the figure GUI manager.
# Pyplot module is mainly intended for
# interactive plots and simple cases of
# programmatic plot generation.
# Here we are also importing random package
# which is used random numbers within the given range.
# Here we are also importing argparse
# which is a command-line argument
# parsing library which we are using here
# to parse path to our image files here.

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--InputImage", required=False, default="imagetr.jpg", help="path to input image file to be read")
args = vars(ap.parse_args())

imgOrignal = cv2.imread(args["InputImage"])
imgOrignal = cv2.cvtColor(imgOrignal, cv2.COLOR_BGR2RGB)
# Here in the above statement we are converting our
# image from the BGR color space to the RGB
# color space.

imgGrey = cv2.cvtColor(imgOrignal, cv2.COLOR_RGB2GRAY)
# Here in the above statement we are converting our
# image from the RGB color space to the Greyscale image

# The below function contains the logic
# for adding salt and pepper noise in
# our input image.
def salt_and_pepper_noise(input_image):
    # the following function.shape is used for
    # getting the dimensions of the image
    row, col = input_image.shape

    # Here we are randomly picking number of
    # pixels in the image for coloring them
    # white.
    # This below randon.randint() function pick a random number
    # between the given values two values here we have taken 100 and 8000
    number_of_pixels = random.randint(200, 8000)
    for i in range(number_of_pixels):
        # Pick a random pont on y coordinate
        y_coordinate = random.randint(0, row - 1)

        # Pick a random point on x coordinate
        x_coordinate = random.randint(0, col - 1)

        # Here we are assigning that pixel white color
        input_image[y_coordinate][x_coordinate] = 255

    # Here we are randomly picking number of
    # pixels in the image for coloring them
    # black.
    # This below randon.randint() function pick a random number
    # between the given values two values here we have taken 200 and 8000
    number_of_pixels = random.randint(200, 8000)
    for i in range(number_of_pixels):
        # Pick a random point y coordinate
        y_coordinate = random.randint(0, row - 1)

        # Pick a random point on x coordinate
        x_coordinate = random.randint(0, col - 1)

        # Here we are assigning that pixel black color
        input_image[y_coordinate][x_coordinate] = 0

    # This below statement returns the output
    # image ndarray with salt and pepper noise in it.
    return input_image

# The below function contains the logic
# for removal of salt and pepper noise from
# our image.
def salt_and_pepper_noise_removed(input_image):
    # This below cv2.medianBlur() function
    # applies the median filter with a
    # kernel specified size which is here set
    # to 3 as per our requirements to our image
    # that contains salt and pepper noise.
    median_blured_image = cv2.medianBlur(input_image, 3)

    # This below statement returns the output
    # image ndarray with salt and pepper noise
    # removed from it.
    return median_blured_image


noisedImage = salt_and_pepper_noise(imgGrey)
removedNoiseImage = salt_and_pepper_noise_removed(noisedImage)

imagesTitle = ["Orignal Image", "Noised(Salt and Pepper) Image", "Removed noise Image"]
imagesBoth = [imgOrignal, noisedImage, removedNoiseImage]

for i in range(3):
    plt.subplot(1, 3, i + 1), plt.imshow(imagesBoth[i], 'gray')
    plt.title(imagesTitle[i])

plt.show()
