import cv2
# This import statement is used to import the python packages or modules that required by our program.
# Here we are importing cv2 module which is used for imgOrignal reading and also for displaying imgOrignal in our program.
# opencv read the images a numpy arrays.

img = cv2.imread("imagetr.jpg")
# cv2.imread() function is used to read and load imgOrignal files stored in your system.

scalingPercentage = 115
# This above scaligPercentage variable has the percentage value
# by which the imgOrignal has to be resized.

newWidth = int(img.shape[1] * scalingPercentage / 100)
newHeight = int(img.shape[0] * scalingPercentage / 100)
# These above two statements calculate the new height and
# width of the new resized imgOrignal. which depends on the
# scaling factor that we are using.

dim = (newWidth, newHeight)
# This is the new dimensions of the upscaled imgOrignal

imgUpscaled = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)
# The above cv2.resize() function is used to resize the imgOrignal src down to or up to the specified size.

print("Original imgOrignal dimensions: ", img.shape)
# This above imgOrignal prints the imgOrignal dimensions of actual imgOrignal.

print("New Resized imgOrignal dimensions: ", imgUpscaled.shape)
# This above print statement prints the upscaled imgOrignal dimensions.

cv2.imshow("Orignal Image (640 x 640)", img)
cv2.imshow("Upsampled/Upscaled imgOrignal", imgUpscaled)

cv2.waitKey(0)
# cv2.waitKey() function waits for a couple of seconds as specified by the user for a key event.
# Here as we have defined zero here then the waitKey() function waits infinitely for a key event to happen.

cv2.destroyAllWindows()
# This cv2.destroyAllWindows() function destroys all the opened GUI windows which are opened
# by this particular  program.