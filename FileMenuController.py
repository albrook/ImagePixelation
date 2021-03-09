"""
A script that is used as a controller for the script GUI.py
This script primarily focuses on the file tab in GUI.py, and hence contains methods for opening an image and saving an image.

Author: Alan Brook
Date: March 2021
"""

from tkinter import filedialog
import ImportExportImages as IEI
import ImageColour as IC
import Globals

importExportImages = IEI.ImportExport()

def openImage(colour, width, height):
    """
    Given a enum for the type of image to be loaded (Unchanged, RGB, Grayscale) calls the relevant methods in the ImportExportImages script.
    :param colour {ENUM}: An enum depicting how the image will be loaded.
    :return: image, {numpyArray}, filename {String}: An array the describes the image, and the name of the file it is saved in. None if the selected option is not supported.
    """
    importExportImages.fitToScreen(width, height)
    filename = filedialog.askopenfilename()
    alteredImageFilename = Globals.localSaveFilename
    if colour == IC.ImageColour.UNCHANGED:
        image = importExportImages.importUnchangedImage(filename)
    elif colour == IC.ImageColour.COLOUR:
        image = importExportImages.importColourImage(filename)
    elif colour == IC.ImageColour.GRAYSCALE:
        image = importExportImages.importGrayscaleImage(filename)
    else:
        print("The option you selected is not currently supported")
        return None, None

    importExportImages.exportChangedImage(image)
    image = importExportImages.importUnchangedImage(alteredImageFilename)
    return image, alteredImageFilename


def saveImage(image):
    """
    Asks for a name to save the image, then passes on the name and image to the relevant method in the ImportExportImages script.
    :param image {numpyArray}: The array to be saved as a picture
    :return: {Boolean}: True if the image saves successfully. False otherwise.
    """
    filetypes = [('JPEG', ('*.jpg', '*.jpeg')), ('PNG', '*.png')]
    name = filedialog.asksaveasfilename(title="Select file", filetypes=filetypes, defaultextension=filetypes)
    return importExportImages.exportImage(name, image)

