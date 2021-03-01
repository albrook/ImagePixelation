from tkinter import filedialog
import ImportExportImages as IEI
import ImageColour as IC

importExportImages = IEI.ImportExport()

def openImage(colour):
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

def saveImage(image):
    filetypes = [('JPEG', ('*.jpg', '*.jpeg')), ('PNG', '*.png')]
    name = filedialog.asksaveasfilename(title="Select file", filetypes=filetypes, defaultextension=filetypes)
    importExportImages.exportImage(name, image)

