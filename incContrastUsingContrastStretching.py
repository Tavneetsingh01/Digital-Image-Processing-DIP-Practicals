from PIL import Image
# PIL library is imported to do imgOrignal manipulations

def normalizeRedChanel(intensity):
    iI = intensity
    # Here this iI holds the value of input pixel of imgOrignal.

    minI = 75
    # Here this minI hold the minimum pixel value of red channel of input imgOrignal.

    maxI = 230
    # Here this maxI hold the maximum pixel value of red channel of input imgOrignal.

    minO = 0
    # Here this minO hold the minimum pixel value of red channel that we want
    # to get in our output imgOrignal.

    maxO = 255
    # Here this maxO hold the maximum pixel value of red channel that we want
    # to get in our output imgOrignal.

    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    # This above if the formula for doing contrast transformation imgOrignal

    return iO

def normalizeGreenchannel(intensity):
    iI = intensity
    # Here this iI holds the value of input pixel of imgOrignal.

    minI = 90
    # Here this minI hold the minimum pixel value of green channel of input imgOrignal.

    maxI = 225
    # Here this maxI hold the maximum pixel value of green channel of input imgOrignal.

    minO = 0
    # Here this minO hold the minimum pixel value of green channel that we want
    # to get in our output imgOrignal.

    maxO = 255
    # Here this maxO hold the maximum pixel value of green channel that we want
    # to get in our output imgOrignal.

    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)

    return iO

def normalizeBluechannel(intensity):
    iI = intensity
    # Here this iI holds the value of input pixel of imgOrignal.

    minI = 100
    # Here this minI hold the minimum pixel value of blue channel of input imgOrignal.

    maxI = 210
    # Here this maxI hold the maximum pixel value of blue channel of input imgOrignal.

    minO = 0
    # Here this minO hold the minimum pixel value of blue channel that we want
    # to get in our output imgOrignal.

    maxO = 255
    # Here this maxO hold the maximum pixel value of blue channel that we want
    # to get in our output imgOrignal.

    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)

    return iO


img = Image.open("imagetr.jpg")
# This Image.open() function is used in PIL library for loading of
# specified imgOrignal from the filesystem.

multiBands = img.split()
# This above .split() method of PIL is used to split imgOrignal into
# its different channels.
# Here as our input imgOrignal is an RGB imgOrignal so, this .split() function
# splits our imgOrignal into three different images each containing a
# copy of one of the original channels (red, green,and blue).

normalizedRedChannel = multiBands[0].point(normalizeRedChanel)
normalizedGreenChannel = multiBands[1].point(normalizeGreenchannel)
normalizedBlueChannel = multiBands[2].point(normalizeBluechannel)
# Here .point() function is used to do point operation on the
# individual pixel of each color channels of the imgOrignal.
# These point operations does the contrast Stretching of
# the each color channels of the imgOrignal.

imageWithIncreasedContrast = Image.merge("RGB", (normalizedRedChannel, normalizedGreenChannel, normalizedBlueChannel))
# This  Image.merge() fuction merges the seperated color channels back together.

img.show("Orignal Image")
# The above statement is used to display the imgOrignal before imgOrignal processing

imageWithIncreasedContrast.show("Contrast Inc Image")
# This above statement is used to show imgOrignal having its
# contrast stretched using Contrast stretching technique.
