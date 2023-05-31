import cv2
# This import statement is used to import the python packages or modules that required by our program.
# Here we are importing cv2 module which is used for imgOrignal reading and also for displaying imgOrignal in our program.
# opencv read the images a numpy arrays.

import argparse
# argparse is a command-line argument parsing library.

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imgOrignal", required=True, help="path to input imgOrignal file to be read")
args = vars(ap.parse_args())

img = cv2.imread(args["imgOrignal"])
# without arguments we do :- imgOrignal = cv2.imread("imagetr.jpg")
# cv2.imread() function is used to read and load imgOrignal files stored in your system.

cv2.imshow("input imgOrignal through command-line", img)
# cv2.imshow() function is used to display the imgOrignal in the specified window.

print(type(img))
# The above print statement shows us the type of variable imgOrignal is.

print(img.shape)
# This above print command prints to the terminal the imgOrignal dimensions and also the number
# of color channels an imgOrignal has.

print(img)
# As we know that the opencv reads the images as a numpy array so this print command displays
# the numpy array values for each pixel in the imgOrignal.

cv2.waitKey(0)
# cv2.waitKey() function waits for a couple of seconds as specified by the user for a key event.
# Here as we have defined zero here then the waitKey() function waits infinitely for a key event to happen.
cv2.destroyAllWindows()
# This cv2.destroyAllWindows() function destroys all the opened GUI windows which are opened
# by this particular  program.
