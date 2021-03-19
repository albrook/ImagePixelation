import numpy as np

"""
A script that contains my own pixelation algorithm. Inspiration is taken from Lee and Frost Diffusion, where a "window"
of pixels is taken, and an average colour value of all the pixels is calculated. All pixel in the window are then set to
the average colour.

Author: Alan Brook
Date: March 2021
"""

import cv2 as cv
import Globals

def pixelation(filename):
    """
    The master method for the algorithm. Describes the flow of the algorithm, while smaller methods, findAverage and
    getPixelWindow deal with the calculations.

    The algorithm works by iterating through the image's array after being loaded into the program. The window size depends on the user, default is 7x7.
    The algorithm iterates through every 7th height and width pixels, collects the targeted pixels (getPixelWindow), then finds the average colour (findAverage).
    Finally, all pixels in the designated window are changed to the average colour, and the next iteration begins.

    :param filename (String): The route to the image file to be used in the algorithm.
    :return: (numpy array): The array of the pixelated image.
    """
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
    """
    Given a list of all of the pixel colours in RGB format, finds the average value.
    :param pixels (List): A list of pixels in [R,G,B] format
    :return: [List]: a list consisting three values which correspond to R,G,B.
    """
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
    """
    Given a pixel coordinate in the format (x,y), a list of an image's pixels and the radius from the centre to the edge of a
    window, returns a list containing all pixels within said window.
    :param center (Tuple): A coordinate in the format (x,y) that denotes the center of the window.
    :param image (List): The image that is being transformed in List format.
    :param windowDifference (int): Th radius of the window. Ex, if the window is 7x7, the the windowdifference will be 3
    :return (List): a list of all the pixels and their pixel values within the window.
    """
    window = []

    for windowWidth in range(center[0] - windowDifference, center[0] + windowDifference):
        for windowHeight in range(center[1] - windowDifference, center[1] + windowDifference):
            if windowHeight < image.shape[0] and windowWidth < image.shape[1]:
                try:
                    window.append(image[windowHeight][windowWidth])
                except IndexError:
                    print(windowWidth, windowHeight)
    return window


#========================================
#Pixelate and Shrink Variation

def pixelateAndShrink(filename):
    """
    A variation of the base pixelation algorithm.

    The algorithm works by iterating through the image's array after being loaded into the program. The window size depends on the user, default is 7x7.
    The algorithm iterates through every 7th height and width pixels, collects the targeted pixels (getPixelWindow), then finds the average colour (findAverage).
    Finally, the window is converted to one pixel, and set to the average pixel colour. All the pixels are then added to a list, which is converted to a numpy array.

    :param filename (String): The route to the image file to be used in the algorithm.
    :return: (numpy array): The array of the pixelated and shrunken image.
    """

    image = cv.imread(filename, cv.IMREAD_COLOR)
    newImageArray = []

    width = image.shape[1]
    height = image.shape[0]

    windowDifference =  Globals.pixelationWindowPixels//2
    for j in range(windowDifference, height, Globals.pixelationWindowPixels):
        row = []
        for i in range(windowDifference, width, Globals.pixelationWindowPixels):
            window = getPixelWindow((i,j), image, windowDifference)
            average = findAverage(window)
            row.append(average)
        newImageArray.append(row)


    newImage = np.array(newImageArray)
    return newImage