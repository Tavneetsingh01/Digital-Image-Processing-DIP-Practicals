import cv2

# This import statement is used to import the python packages or modules that required by our program.
# Here we are importing cv2 module which is used for imgOrignal reading and also for displaying imgOrignal in our program.
# opencv read the images a numpy arrays.
# As our images are read in the form of numpy array.
from matplotlib import pyplot as plt

img = cv2.imread("imagetr.jpg")
# cv2.imread() function is used to read and load imgOrignal files stored in your system.

img = cv2.resize(img, (320, 214))
# cv2.resize() function resizes the input imgOrignal into the provided height and width.

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.ctvColor() function converts the input imgOrignal from one color space to
# another color space by provided the desired argument.
# Here we are converting imgOrignal from BGR color space to a greyscale imgOrignal

histogramEquilizedImage = cv2.equalizeHist(imgGrey)

cv2.imshow("orignal imgOrignal", img)
cv2.imshow("Greyscale imgOrignal of input imgOrignal", imgGrey)
cv2.imshow("Histogram Equalized imgOrignal of input imgOrignal", histogramEquilizedImage)
# cv2.imshow() function is used to display the imgOrignal in the specified window.

inputImageHistogram = cv2.calcHist([img], [0, 1, 2], [256], None, [0, 256])


cv2.waitKey(0)
# cv2.waitKey() function waits for a couple of seconds as specified by the user for a key event.
# Here as we have defined zero here then the waitKey() function waits infinitely for a key event to happen.

cv2.destroyAllWindows()
# This cv2.destroyAllWindows() function destroys all the opened GUI windows which are opened
# by this particular  program.
plt.plot(inputImageHistogram)
plt.show()