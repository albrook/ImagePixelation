import cv2 as cv

def binary_threshold(filename):
    """
    Performs Binary Thresholding on the given file.
    :param filename: (String) The name of the file that Binary Threshold is to be performed on
    :param edited_filename: (String)The filename to be of the transformed image
    :return: (numpy array) An array of the transformed image in red-green-blue format
    """
    image = cv.imread(filename, cv.IMREAD_GRAYSCALE)
    ret, thresh1 = cv.threshold(image, 90, 255, cv.THRESH_BINARY)
    return thresh1