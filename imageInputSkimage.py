import matplotlib.pyplot as plt
from skimage import io
# This import statement is used to import the python packages or modules that required by our program.
# Here we are importing skimage module which is used for imgOrignal reading, imgOrignal manipulation
# and also for displaying imgOrignal in our program.
# Here also we are importing matplotlib.pyplot
# skimage read the images a numpy arrays.
# Here we are also importing matplotlib.pyplot which provides an implicit, MATLAB-like, way of plotting.
# It also used to opens figures on your screen, and also acts as the figure GUI manager.
# pyplot module is mainly intended for interactive plots and simple cases of programmatic plot generation.
# Here we are using matplotlib.pyplot to display title on our output imgOrignal.

img = io.imread("imagetr.jpg")
# io.imread() function of skimage isused to read  images from a file system / from a url.

print(type(img))
# The above print statement shows us the type of variable imgSngl is.

print(img.shape)
# This above print command prints to the terminal the imgOrignal dimensions and also the number
# of color channels an imgOrignal has.

print(img)
# As we know that the skimage.io.imread() function reads the images as a numpy array so this print command displays
# the numpy array values for each pixel in the imgOrignal.

plt.title("Image Input Using Skimage library")
# Here plt.title() function is used to display title on the output imgOrignal plot.

io.imshow(img)
# io.imshow() is used to display the imgOrignal

io.show()
# io.show() Launch the event loop of the current gui plugin, and display all pending images, queued via imshow.
# A call to show will block execution of code until all windows have been closed.
# this io.show() is required when we are using imshow in non-interactive scripts.
