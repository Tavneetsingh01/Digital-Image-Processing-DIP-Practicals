import math

import cv2
import numpy as np
# This import statement is used to import the python packages or
# modules that required by our program.
# Here we are importing cv2 module which is used for imgOrignal
# reading and also for displaying imgOrignal in our program
# Here we are also importing numpy which is used to do
# manipulation on array objects.
# Here we are using this library to manipulate our
# numpy array of image as Opencv read the images a
# numpy arrays.
image = cv2.imread('imagetr.jpg')
# cv2.imread() function is used to read and load imgOrignal files stored in your system.

image = cv2.resize(image, (320, 320))
# The above cv2.resize() function is used to resize the imgOrignal
# src down to or up to the specified size.

c = 255/math.log(1+np.max(image))
print(c)

print(np.max(image))

cv2.imshow("orignal image", image)
# cv2.imshow() function is used to display the imgOrignal in the specified window.

# list of Gamma values to be taken
for gammaValues in [1, 1.5, 1.8, 2.5, 3.0, 5.0]:
    # Applying the power law transformation on image numpy array.
    gammaTransformedImg = np.array(255 * (image / 255) ** gammaValues, dtype='uint8')

    cv2.imshow('imgWithGammaValue = ' + str(gammaValues), gammaTransformedImg)
    # cv2.imshow() function is used to display the imgOrignal in the specified window.

cv2.waitKey(0)
# cv2.waitKey() function waits for a couple of seconds
# as specified by the user for a key event.
# Here as we have defined zero here then the waitKey()
# function waits infinitely for a key event to happen.

cv2.destroyAllWindows()
# This cv2.destroyAllWindows() function destroys all the opened GUI windows which are opened
# by this particular  program.
