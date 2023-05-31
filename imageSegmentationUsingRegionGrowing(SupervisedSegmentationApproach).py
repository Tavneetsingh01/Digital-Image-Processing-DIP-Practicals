import cv2
import numpy as np
import argparse
# This import statement is used to import the python packages or
# modules that required by our program.
# Here we are importing cv2 module which is used for image
# reading and also for displaying images.
# opencv read the images a numpy arrays.
# Here we are also importing argparse
# which is a command-line argument
# parsing library which we are using here
# to parse path to our image files here.
class Stack():
    def __init__(self):
        self.item = []
        self.obj = []

    def push(self, value):
        self.item.append(value)

    def pop(self):
        return self.item.pop()

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.size() == 0

    def clear(self):
        self.item = []


class regionGrow():

    def __init__(self, image_path, th_value):
        self.readImage(image_path)
        self.h, self.w, _ = self.im.shape
        self.passedBy = np.zeros((self.h, self.w), np.double)
        self.currentRegion = 0
        self.iterations = 0
        self.SEGS = np.zeros((self.h, self.w, 3), dtype='uint8')
        self.stack = Stack()
        self.thresh = float(th_value)

    def readImage(self, img_path):
        self.im = cv2.imread(img_path, 1)

    def getNeighbour(self, x0, y0):
        neighbour = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if (i, j) == (0, 0):
                    continue
                x = x0 + i
                y = y0 + j
                if self.limit(x, y):
                    neighbour.append((x, y))
        return neighbour

    def ApplyRegionGrow(self, seeds):
        temp = []
        for i in seeds:
            temp.append(i)
            temp.extend(self.getNeighbour(i[0], i[1]))
        seeds = temp
        for i in (seeds):
            x0 = int(i[0])
            y0 = int(i[1])

            if self.passedBy[x0, y0] == 0 and (
                    int(self.im[x0, y0, 0]) * int(self.im[x0, y0, 1]) * int(self.im[x0, y0, 2]) > 0):
                self.currentRegion += 1
                self.passedBy[x0, y0] = self.currentRegion
                self.stack.push((x0, y0))
                while not self.stack.isEmpty():
                    x, y = self.stack.pop()
                    self.BFS(x, y)
                    self.iterations += 1
                if (self.PassedAll()):
                    break
                count = np.count_nonzero(self.passedBy == self.currentRegion)
                if (count < 8 * 8):
                    self.passedBy[self.passedBy == self.currentRegion] = 0
                    x0 -= 1
                    y0 -= 1
                    self.currentRegion -= 1

        for i in range(0, self.h):
            for j in range(0, self.w):
                val = self.passedBy[i][j]
                if (val == 0):
                    self.SEGS[i][j] = 255, 255, 255
                else:
                    self.SEGS[i][j] = val * 35, val * 90, val * 30
        if (self.iterations > 200000):
            print("Max Iterations")
        print("Iterations : " + str(self.iterations))
        cv2.imshow("Segmented Image", self.SEGS)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def BFS(self, x0, y0):
        regionNum = self.passedBy[x0, y0]
        elems = []
        elems.append((int(self.im[x0, y0, 0]) + int(self.im[x0, y0, 1]) + int(self.im[x0, y0, 2])) / 3)
        var = self.thresh
        neighbours = self.getNeighbour(x0, y0)

        for x, y in neighbours:
            if self.passedBy[x, y] == 0 and self.distance(x, y, x0, y0) < var:
                if (self.PassedAll()):
                    break;
                self.passedBy[x, y] = regionNum
                self.stack.push((x, y))
                elems.append((int(self.im[x, y, 0]) + int(self.im[x, y, 1]) + int(self.im[x, y, 2])) / 3)
                var = np.var(elems)
            var = max(var, self.thresh)

    def PassedAll(self):

        return self.iterations > 200000 or np.count_nonzero(self.passedBy > 0) == self.w * self.h

    def limit(self, x, y):
        return 0 <= x < self.h and 0 <= y < self.w

    def distance(self, x, y, x0, y0):
        return ((int(self.im[x, y, 0]) - int(self.im[x0, y0, 0])) ** 2 + (
                int(self.im[x, y, 1]) - int(self.im[x0, y0, 1])) ** 2 + (
                        int(self.im[x, y, 2]) - int(self.im[x0, y0, 2])) ** 2) ** 0.5


def Check_Mouse_Clicks(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.destroyAllWindows()

    if event == cv2.EVENT_LBUTTONDOWN:
        seeds.append([y, x])


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--INPUTIMAGE", required=True, help="path to input image file to be read")
ap.add_argument("-th", "--THRESHOLDVALUE", required=False, default=10, help="enter the threshold value")
args = vars(ap.parse_args())
seeds = []
supervisedSegmentationProgram = regionGrow(args["INPUTIMAGE"], args["THRESHOLDVALUE"])
cv2.namedWindow("Non-Segmented input image (choose the initial seeds from the image by pressing left click button)")
cv2.setMouseCallback(
    "Non-Segmented input image (choose the initial seeds from the image by pressing left click button)", Check_Mouse_Clicks)
cv2.imshow("Non-Segmented input image (choose the initial seeds from the image by pressing left click button)",
           cv2.imread(args["INPUTIMAGE"], 1))
cv2.waitKey(0)

# The below given statement call function ApplyRegionGrow(seeds)
# and starts our program execution.
# the function
# Here the function ApplyRegionGrow(seeds) is the main function
# of our program. this function takes seeds as its parameter.
# These seeds are selected by the user.
supervisedSegmentationProgram.ApplyRegionGrow(seeds)
