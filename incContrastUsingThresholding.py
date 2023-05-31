import cv2
# This import statement is used to import the python packages or modules that required by our program.
# Here we are importing cv2 module which is used for imgOrignal reading and also for displaying imgOrignal in our program.
# opencv read the images a numpy arrays.
# As our images are read in the form of numpy array.

img = cv2.imread("imagetr.jpg")
# cv2.imread() function is used to read and load imgOrignal files stored in your system.

img = cv2.resize(img, (320, 320))
# cv2.resize() function resizes the input imgOrignal into the provided height and width.

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.ctvColor() function converts the input imgOrignal from one color space to
# another color space by provided the desired argument.
# Here we are converting imgOrignal from BGR color space to a greyscale imgOrignal

(thresh1, imgIncreasedContrast) = cv2.threshold(img, 123, 255, cv2.THRESH_BINARY)
# cv2.threshhold() function applies fixed-level thresholding to a
# multiple-channel array (which is our greyscale imgOrignal (imgGrey) here.
# This  function is typically used to get a bi-level (binary) imgOrignal
# out of a grayscale imgOrignal or for removing a noise, that is,
# filtering out pixels with too small or too large values.
# There are several types of thresholding supported by the function.
# They are determined by type parameter.

cv2.imshow("orignal imgOrignal", img)
cv2.imshow("Greyscale imgOrignal of input imgOrignal", imgGrey)
cv2.imshow("Increased contrast Image", imgIncreasedContrast)
# cv2.imshow() function is used to display the imgOrignal in the specified window.

cv2.waitKey(0)
# cv2.waitKey() function waits for a couple of seconds as specified by the user for a key event.
# Here as we have defined zero here then the waitKey() function waits infinitely for a key event to happen.

cv2.destroyAllWindows()
# This cv2.destroyAllWindows() function destroys all the opened GUI windows which are opened
# by this particular  program.