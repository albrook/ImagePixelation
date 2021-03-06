import cv2 as cv
import Globals

def Pixelation(filename):
    image = cv.imread(filename, cv.IMREAD_COLOR)

    width = image.shape[1]
    height = image.shape[0]

    windowDifference =  Globals.pixelationWindowPixels//2
    for i in range(windowDifference, width, Globals.pixelationWindowPixels):
        for j in range(windowDifference, height, Globals.pixelationWindowPixels):
            window = getPixelWindow((i,j), image, windowDifference)
            average = findAverage(window)
            for windowWidth in range(i-windowDifference, i+windowDifference):
                for windowHeight in range(j-windowDifference, j+windowDifference):
                    try:
                        image[windowHeight][windowWidth] = average
                    except IndexError:
                        pass
    return image

def findAverage(pixels):
    red, green, blue = 0, 0, 0
    count = 0
    for i in pixels:
        red += i[0]
        green += i[1]
        blue += i[2]
        count += 1
    if pixels == []:
        return [0,0,0]
    else:
        return [int(red/count), int(green/count), int(blue/count)]

def getPixelWindow(center, image, windowDifference):
    window = []

    for windowWidth in range(center[0] - windowDifference, center[0] + windowDifference):
        for windowHeight in range(center[1] - windowDifference, center[1] + windowDifference):
            if windowHeight < image.shape[0] and windowWidth < image.shape[1]:
                try:
                    window.append(image[windowHeight][windowWidth])
                except IndexError:
                    print(windowWidth, windowHeight)
    return window
