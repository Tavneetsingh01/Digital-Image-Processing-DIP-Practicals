import cv2
import numpy as np

# This import statement is used to import the python packages or modules that required by our program.
# Here we are importing cv2 module which is used for imgOrignal reading and also for displaying imgOrignal in our program.
# opencv read the images a numpy arrays.
# numpy is used to do manipulation on array object (which are Images here).
# As our images are read in the form of numpy array.

img = cv2.imread("imagetr.jpg")
# cv2.imread() function is used to read and load imgOrignal files stored in your system.

# imgOrignal=cv2.resize(imgOrignal,(320,556)) for imgOrignal.jpg
# imgOrignal = cv2.resize(imgOrignal, (320, 214)) for imagergb1.jpg
img = cv2.resize(img, (320, 320)) # for imagetr.jpg
# imgOrignal = cv2.resize(imgOrignal, (360, 360)) for RGB imgOrignal
# cv2.resize() function resizes the input imgOrignal into the provided height and width.

cv2.imshow("orignal imgOrignal", img)
# cv2.imshow() function is used to display the imgOrignal in the specified window.

imgr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.ctvColor() function converts the input imgOrignal fron one color space to
# another color space by provided the desired argument.
# Here we are converting imgOrignal from BGR color space to RGB color space.

red, green, blue = cv2.split(imgr)
# cv2.split() function is used to split an imgOrignal into its different color channels.
# This cv2.split() function splits the input imgOrignal in BGR format when we give it a
# imgOrignal without converting its nd array to RGB using CV2.COLOR_BGR2RGB function.
# This is because the cv2.imread() function reads imgOrignal as numpy array in  the BGR format.

zeros = np.zeros(imgr.shape[:2], dtype="uint8")
# np.zeros() function return a new array of given shape ( here shape of our
# input imgOrignal i.e; imgr) and type, filled with zeros.

cv2.imshow("Red channel of imgOrignal", red)
cv2.imshow("Green channel of imgOrignal", green)
cv2.imshow("Blue channel of imgOrignal", blue)
cv2.imshow("Visualized Red channel of imgOrignal", cv2.merge([zeros, zeros, red]))
cv2.imshow("Visualized Green channel of imgOrignal", cv2.merge([zeros, green, zeros]))
cv2.imshow("Visualized Blue channel of imgOrignal", cv2.merge([blue, zeros, zeros]))
# cv2.merge() function is used to merge numpy arrays.
# Here we are using cv2.merge() function to merge color channels of imgOrignal.


cv2.waitKey(0)
# cv2.waitKey() function waits for a couple of seconds as specified by the user for a key event.
# Here as we have defined zero here then the waitKey() function waits infinitely for a key event to happen.

cv2.destroyAllWindows()
# This cv2.destroyAllWindows() function destroys all the opened GUI windows which are opened
# by this particular  program.


# (h, w) = imgOrignal.shape[:2]
# output = np.zeros((h * 2, w * 2, 3), dtype="uint8")
# output[0:h, 0:w] = imgOrignal
# output[0:h, w:w * 2] = redimg
# utput[h:h * 2, w:w * 2] = greenimg
# output[h:h * 2, 0:w] = blueimg
# cv2.imshow("blue channel of imgOrignal",output)
