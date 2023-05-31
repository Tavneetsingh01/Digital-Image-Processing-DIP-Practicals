import cv2
import numpy as np
import argparse
# This import statement is used to import the python packages or
# modules that required by our program.
# Here we are importing cv2 module which is used for image
# reading and also for displaying images in our program.
# opencv read the images a numpy arrays.
# opencv read the images a numpy arrays.
# Here we are also importing numpy is
# used to do manipulation on array object
# (which are Images here).
# Here we are also importing argparse
# which is a command-line argument
# parsing library which we are using here
# to parse path to our image files here.

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--InputImage", required=False, default="imagetr.jpg", help="path to input image file to be read")
args = vars(ap.parse_args())

img = cv2.imread(args["InputImage"])
# The above function cv2.imread is used
# to read the images from the disk.

# The below Scale Percentage represents
# the scale of original size of image we want.
scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dimensions = (width, height)
img = cv2.resize(img, dimensions, cv2.INTER_AREA)
# The above function cv2.resize is used
# to resize the images as per our
# requirements(HxW).

img_orignal_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Here in the above statement we are converting our
# image from the BGR color space to the RGB
# color space.

# This below function Defines the code for converting
# an image from RGB(Red, Green, and Blue) color space
# to HSI(Hue, Saturation , and Intensity) color space.


def RGB2HSI(input_rgb_image):
    # Below statement is used to
    # separate the individual R, G and B
    # channels present in input image.
    r, g, b = input_rgb_image[:, :, 0], input_rgb_image[:, :, 1], input_rgb_image[:, :, 2]

    # Below statement is used to calculate
    # the sum of all the channels i.e; R, G and B
    sm = np.sum(input_rgb_image, axis=2)

    # Below statement calculates the intensity value from RGB image.
    i = sm / 3

    # Below statement calculates the saturation value from RGB image.
    s = 1 - (np.min(input_rgb_image, axis=2) / sm * 3)

    r = r.astype(np.float16)
    g = g.astype(np.float16)
    b = b.astype(np.float16)

    num = (2 * r - g - b)
    den = 2 * np.sqrt(np.square(r - g) + (r - b) * (g - b))

    t = np.ones(b.shape, dtype=int)
    t = np.divide(num, den, where=den != 0)
    t = np.degrees(np.arccos(t))

    # Below statement is used to calculate the value of Hue.
    h = np.where(b > g, 360 - t, t)

    hsi_image = np.dstack([h, s, i])

    # Here in the below return statement we
    # are returning ndarray of our HSI image.
    return hsi_image

# This below function Defines the code for converting
# an image from HSI(Hue, Saturation , and Intensity) color space
# to RGB(Red, Green, and Blue)color space.


def HSI2RGB(input_hsi_image):
    h, s, i = input_hsi_image[:, :, 0], input_hsi_image[:, :, 1], input_hsi_image[:, :, 2]

    # initialise rgb matrices to zero
    r = np.zeros(h.shape, dtype=int)
    g = np.zeros(h.shape, dtype=int)
    b = np.zeros(h.shape, dtype=int)

    # In the following statements we are
    # calculating r,g,b chanel values from h,s,i values.
    t = i * (1 - s)
    b = np.where(h < 120, t, b)
    r = np.where((120 <= h) & (h < 240), t, r)
    g = np.where(h > 240, t, g)

    t = s * (np.cos(np.radians(h)) / np.cos(np.radians(60 - h)))
    r = np.where(h < 120, i * (1 + t), r)

    t = s * (np.cos(np.radians(h - 120)) / np.cos(np.radians(180 - h)))
    g = np.where((120 <= h) & (h < 240), i * (1 + t), g)

    t = s * (np.cos(np.radians(h - 240)) / np.cos(np.radians(300 - h)))
    b = np.where(h > 240, i * (1 + t), b)

    g = np.where(h < 120, 3 * i - r - b, g)
    b = np.where((120 <= h) & (h < 240), 3 * i - r - g, b)
    r = np.where(h > 240, 3 * i - g - b, r)

    # In the below statement we are concatenated
    # rgb channels and round to 8-bit unsigned
    # integer (range 0-255)
    rgb_img = np.round(np.dstack([b, g, r]))
    rgb_img = rgb_img.astype(np.uint8)

    # Here in the below return statement we
    # are returning ndarray of our RGB image.
    return rgb_img

# This below function Defines the code for converting
# an image from RGB(Red, Green, and Blue) color space
# to CMY(Cyan, Magenta and Yellow) color space.

def RGB2CMY(input_rgb_image):
    # Below statement is used to
    # separate the individual R, G and B
    # channels present in input image.
    r, g, b = input_rgb_image[:, :, 0], input_rgb_image[:, :, 1], input_rgb_image[:, :, 2]

    # cmy_image = 1 - (rgb_image/255)
    c = 1 - (r / 255)
    m = 1 - (g / 255)
    y = 1 - (b / 255)

    cmy_image = np.dstack([c, m, y])

    # Here in the below return statement we
    # are returning ndarray of our CMY image.
    return cmy_image

# This below function Defines the code for converting
# an image from CMY(Cyan, Magenta and Yellow) color space
# to RGB(Red, Green, and Blue)color space.


def CMY2RGB(input_cmy_image):
    # rgb_image = 1 - input_cmy_image
    c, m, y = input_cmy_image[:, :, 0], input_cmy_image[:, :, 1], input_cmy_image[:, :, 2]
    r = 1 - c
    g = 1 - m
    b = 1 - y
    rgb_image = np.dstack([b, g, r])

    # Here in the below return statement we
    # are returning ndarray of our CMY image.
    return rgb_image


RGB_to_HSI_image = RGB2HSI(img_orignal_rgb)
HSI_to_RGB_image = HSI2RGB(RGB_to_HSI_image)
RGB_to_CMY_image = RGB2CMY(img_orignal_rgb)
CMY_to_RGB_image = CMY2RGB(RGB_to_CMY_image)

cv2.imshow("Original Image", img)
cv2.imshow("RGB2HSI Image", RGB_to_HSI_image)
cv2.imshow("HSI2RGB Image", HSI_to_RGB_image)
cv2.imshow("RGB2CMY Image", RGB_to_CMY_image)
cv2.imshow("CMY2RGB Image", CMY_to_RGB_image)
# The above statements are used to Display our
# Original RGB image as well images with different
# Color spaces.

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
