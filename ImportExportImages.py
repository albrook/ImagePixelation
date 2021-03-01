import cv2 as cv
from tkinter import filedialog

class ImportExport():

    def __init__(self):
        pass

    def importUnchangedImage(self, filename):
        """

        :return: None
        """
        image = None
        try:
            image = cv.imread(filename)
        except(AttributeError, SystemError):
            print("Failed to import selected file")
        finally:
            return image

    def importColourImage(self, filename):
        """

        :return: None
        """
        image = None
        try:
            image = cv.imread(filename, cv.IMREAD_COLOR)
        except(AttributeError, SystemError):
            print("Failed to import selected file")
        finally:
            return image

    def importGrayscaleImage(self, filename):
        """

        :return: None
        """
        image = None
        try:
            image = cv.imread(filename, cv.IMREAD_GRAYSCALE)
        except(AttributeError, SystemError):
            print("Failed to import selected file")
        finally:
            return image

    def exportImage(self, name, image):
        try:
            cv.imwrite(name, image)
        except Exception:
            print("There was an error saving the image")
            return False
        finally:
            return True

    def exportChangedImage(self, image):
        try:
            cv.imwrite("AlteredImage.jpg", image)
        except Exception:
            print("There was an error saving the image")
            return False
        finally:
            return True


file = ImportExport()
image = file.importGrayscaleImage("test.jpg")
file.exportImage("testExport.jpg", image)
