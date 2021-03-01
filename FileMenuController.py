from tkinter import filedialog
import ImportExportImages as IEI
import ImageColour as IC

importExportImages = IEI.ImportExport()

def openImage(colour):
    """
    Given a enum for the type of image to be loaded (Unchanged, RGB, Grayscale) calls the relevant methods in the ImportExportImages script.
    :param colour {ENUM}: An enum depicting how the image will be loaded.
    :return: image, {numpyArray}, filename {String}: An array the describes the image, and the name of the file it is saved in. None if the selected option is not supported.
    """
    filename = filedialog.askopenfilename()
    alteredImageFilename = "AlteredImage.jpg"
    if colour == IC.ImageColour.UNCHANGED:
        return importExportImages.importUnchangedImage(filename), filename
    elif colour == IC.ImageColour.COLOUR:
        image = importExportImages.importColourImage(filename)
        importExportImages.exportChangedImage(image)
        image = importExportImages.importUnchangedImage(alteredImageFilename)
        return image, alteredImageFilename
    elif colour == IC.ImageColour.GRAYSCALE:
        image = importExportImages.importGrayscaleImage(filename)
        importExportImages.exportChangedImage(image)
        image = importExportImages.importUnchangedImage(alteredImageFilename)
        return image, alteredImageFilename
    else:
        print("The option you selected is not currently supported")
        return None, None

def saveImage(image):
    """
    Asks for a name to save the image, then passes on the name and image to the relevant method in the ImportExportImages script.
    :param image {numpyArray}: The array to be saved as a picture
    :return: {Boolean}: True if the image saves successfully. False otherwise.
    """
    filetypes = [('JPEG', ('*.jpg', '*.jpeg')), ('PNG', '*.png')]
    name = filedialog.asksaveasfilename(title="Select file", filetypes=filetypes, defaultextension=filetypes)
    return importExportImages.exportImage(name, image)

