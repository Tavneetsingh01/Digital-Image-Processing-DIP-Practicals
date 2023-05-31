import cv2
import glob2
# This import statement is used to import the python packages or modules that required by our program.
# Here we are importing cv2 module which is used for imgOrignal reading and also for displaying imgOrignal in our program.
# opencv read the images a numpy arrays.
# glob2 (short for global) module is used to return all file paths that match a specific pattern. In general it
# is used to search files and folders in the filesystem that match a certain pattern as specified by user.

mainPath = "inputimages/"
# This is the base path where our images are located

ext = ['png', 'jpg', 'jpeg', 'webp', 'tiff']
# this ext[] list specifies the type of imgOrignal file extensions we want to read.

constructedPath = []
for e in ext:
    constructedPath.extend(glob2.glob(mainPath + '*.' + e))
# the above for loop is used to get absolute path (eg: inputimages\\image1.jpg) to each imgOrignal file
# stored in the base path folder based on type of extension that we have specified in ext[] list and
# then add it to constructedPath[] list fo next operation.

imgMulti = []
for images in constructedPath:
    img = cv2.imread(images)
    imgMulti.append(img)
# this above for loop reads each imgOrignal and the append its ndarray to the imageMulti[] list

for i, imgSngl in enumerate(imgMulti):
    cv2.imshow("Image Number {}".format(i), imgSngl)
    print(type(imgSngl))
    # The above print statement shows us the type of variable imgSngl is.
    print(imgSngl.shape)
    # This above print command prints to the terminal the imgOrignal dimensions and also the number
    # of color channels an imgOrignal has.

# This above for loop is used for Displaying the images that has been read in the previous step.

print(imgMulti)
# This print statement is used to print the data contained in imgMulti[] list which is ndarray data
# of images that we have read.

cv2.waitKey(0)
# cv2.waitKey() function waits for a couple of seconds as specified by the user for a key event.
# Here as we have defined zero here then the waitKey() function waits infinitely for a key event to happen.

cv2.destroyAllWindows()
# This cv2.destroyAllWindows() function destroys all the opened GUI windows which are opened
# by this particular  program.
