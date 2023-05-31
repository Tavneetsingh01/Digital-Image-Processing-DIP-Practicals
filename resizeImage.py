import cv2
# This import statement is used to import the python packages or modules that required by our program.
# Here we are importing cv2 module which is used for imgOrignal reading and also for displaying imgOrignal in our program.
# opencv read the images a numpy arrays.

img = cv2.imread("imagetr.jpg")
# cv2.imread() function is used to read and load imgOrignal files stored in your system.

imgResize = cv2.resize(img, (320, 320))
# The above cv2.resize() function is used to resize the imgOrignal src down to or up to the specified size.

cv2.imshow("Orignal Image (640 x 640)", img)
# cv2.imshow() function is used to display the imgOrignal in the specified window.
# This above program line is used to display the input imgOrignal in its orignal size.

cv2.imshow("Resized Image (320 x 320)", imgResize)
# This above program line is used to display the resized imgOrignal.

cv2.waitKey(0)
# cv2.waitKey() function waits for a couple of seconds as specified by the user for a key event.
# Here as we have defined zero here then the waitKey() function waits infinitely for a key event to happen.

cv2.destroyAllWindows()
# This cv2.destroyAllWindows() function destroys all the opened GUI windows which are opened
# by this particular  program.
