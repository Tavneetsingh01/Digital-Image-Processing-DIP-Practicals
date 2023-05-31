from sklearn.cluster import MiniBatchKMeans
import cv2
import argparse
# This import statement is used to import
# the python packages or modules that required
# by our program.
# Here we are importing MiniBatchKMeans from
# sklearn.cluster which is the classic
# implementation of the clustering method
# based on the Lloyd's algorithm.
# It consumes the whole set of input
# data at each iteration.
# Here we are also importing cv2 module
# which is used for image reading, manipulation
# and also for displaying images.
# opencv read the images a numpy arrays.
# Here we are also importing argparse
# which is a command-line argument
# parsing library which we are using here
# to parse path to our image files here.


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--InputImage", required=False, default="imagetr.jpg", help="path to input image file to be read")
args = vars(ap.parse_args())

img_original = cv2.imread(args["InputImage"])
# The above function cv2.imread is used
# to read the images from the disk.

# The below Scale Percentage represents
# the scale of original size of image we want.
scale_percent = 50
width = int(img_original.shape[1] * scale_percent / 100)
height = int(img_original.shape[0] * scale_percent / 100)
dimensions = (width, height)
img_original = cv2.resize(img_original, dimensions, cv2.INTER_AREA)
# The above function cv2.resize is used
# to resize the images as per our
# requirements(HxW).

img = img_original

(h, w) = img.shape[:2]

image = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# Here in the above statement we are converting our
# image from the RGB color space to the LAB
# color space. we are doing this because
# in our program we will be clustering the image
# using k-means which is based on the
# euclidean distance, we'll use the LAB color
# space where the euclidean distance implies
# perceptual meaning.

image = image.reshape((img.shape[0] * img.shape[1], 3))
# Here in the above statement we are reshape the
# image into a feature vector so that k-means
# can be applied.
# apply k-means using the specified number of clusters and
# then create the quantized image based on the predictions.

j = 5
for i in range(6):
    clt = MiniBatchKMeans(n_clusters=j)
    labels = clt.fit_predict(image)
    quant = clt.cluster_centers_.astype("uint8")[labels]
    # now in the above statements we are applying
    # k-means using the specified number of clusters and
    # then creating the quantized image based
    # on the predictions.

    quant = quant.reshape((h, w, 3))
    # Now in the above statement we are
    # reshaping the feature vectors to images.

    quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
    # Now in the above statement we are converting
    # our quantized image from LAB color space to RGB
    # color space for displaying.

    cv2.imshow("Img Quantization level of {}".format(j), quant)
    # The above statement is used to displaying our
    # Quantized images having different quantization values.

    j = j + 5

cv2.imshow("Image read with cv2.imread", img)
# The above statement is used to Display our
# Original image read via cv2.imread function.

cv2.waitKey(0)
# cv2.waitKey() function waits for a
# couple of seconds as specified by the
# user for a key event.
# Here as we have defined zero here
# then the waitKey() function waits
# infinitely for a key event to happen.

cv2.destroyAllWindows()
# This cv2.destroyAllWindows() function
# destroys all the opened GUI windows
# which are opened by this particular
# program.
