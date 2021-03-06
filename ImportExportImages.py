import cv2 as cv
import Globals

class ImportExport():
    """
    This class holds methods related to the importing (opening) and exporting (saving) of images.
    Options for opening include opening the image as it is, in colour (RGB) format, and in grayscale.
    There is only one option for saving, as is.
    """
    def __init__(self):
        self.resolutions = [(640, 480), (1280, 720), (1920, 1080)]
        self.width, self.height = 640, 480

    def fitToScreen(self, screenWidth, screenHeight):
        for i in self.resolutions:
            if screenHeight > i[1] or screenWidth > i[0]:
                self.width = i[0]
                self.height = i[1]

    def resizeImage(self, imageToBeResized):
        correctSize = True
        scale_factor = 80
        if self.width < imageToBeResized.shape[1] and self.height < imageToBeResized.shape[0]:
            correctSize = False
        while not correctSize:
            height = int(imageToBeResized.shape[0] * scale_factor / 100)
            width = int(imageToBeResized.shape[1] * scale_factor / 100)
            imageToBeResized = cv.resize(imageToBeResized, (width, height))
            if self.width > len(imageToBeResized[0]) and self.height > len(imageToBeResized):
                correctSize = True
        return imageToBeResized

    def importUnchangedImage(self, filename):
        """
        Given a string filename, attempts to open the file provided. If it fails, feedback is through the command line.
        :param: filename {String}: The name of the file to be opened
        :return: image {numpyArray}: Either a numpy array of the image, or None due to the image failing to load.
        """
        image = None
        try:
            image = cv.imread(filename)
        except(AttributeError, SystemError):
            print("Failed to import selected file")
        finally:
            return self.resizeImage(image)

    def importColourImage(self, filename):
        """
        Given a string filename, attempts to open the file provided in RGB colour. If it fails, feedback is through the command line.
        :param: filename {String}: The name of the file to be opened
        :return: image {numpyArray}: Either a numpy array of the image, or None due to the image failing to load.
        """
        image = None
        try:
            image = cv.imread(filename, cv.IMREAD_COLOR)
        except(AttributeError, SystemError):
            print("Failed to import selected file")
        finally:
            return self.resizeImage(image)

    def importGrayscaleImage(self, filename):
        """
        Given a string filename, attempts to open the file provided in grayscale. If it fails, feedback is through the command line.
        :param: filename {String}: The name of the file to be opened
        :return: image {numpyArray}: Either a numpy array of the image, or None due to the image failing to load.
        """
        image = None
        try:
            image = cv.imread(filename, cv.IMREAD_GRAYSCALE)
        except(AttributeError, SystemError):
            print("Failed to import selected file")
        finally:
            return self.resizeImage(image)

    def exportImage(self, name, image):
        """
        Given a filename, and a numpy array of an image, attempts to save the image.
        If this fails, feedback is through the command line.
        :param: name {String}: Where the image is meant to be saved
        :param: image {numpyArray}: An array of the image to be saved
        :return: {Boolean}: True if the save is successful, False otherwise
        """
        try:
            cv.imwrite(name, image)
        except Exception:
            print("There was an error saving the image")
            return False
        finally:
            return True

    def exportChangedImage(self, image):
        """
        This method is used when different variation of images are loaded into the application, namely colour and grayscale
        images, not when the image is saved through the save option.
        Given a filename, and a numpy array of an image, attempts to save the image.
        If this fails, feedback is through the command line.
        :param: image {numpyArray}: An array of the image to be saved
        :return: {Boolean}: True if the save is successful, False otherwise
        """
        try:
            cv.imwrite(Globals.localSaveFilename, image)
        except Exception:
            print("There was an error saving the image")
            return False
        finally:
            return True

