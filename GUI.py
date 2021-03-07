import tkinter as tk
from PIL import ImageTk,Image, ImageOps
from enum import Enum

import FileMenuController as FMC
import AlgorithmController as AC
import ImageColour as IC
import Algorithm as ALG
import Globals



class FileMenu(Enum):
    """
    An enum that keeps track of the options in the file menu of the GUI
    """
    OPEN = 1
    SAVE = 2
    CLOSE = 3

class GUI(tk.Tk):
    """
    The class that holds all information regarding the GUI and its running.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises a tKinter Gui
        :param args:
        :param kwargs:
        """
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Image Pixelation")
        self.image = None
        self.imageArray = None
        self.imageDimensions = (640, 480)
        self.filename = None
        self.mainFrame = tk.Frame(self).grid(row=0, column=0)
        self.menu = tk.Menu()
        self.initCanvas()
        self.initMenus()
        tk.Tk.config(self, menu=self.menu)

    def initCanvas(self):
        """
        Creates the canvas from which the image will be shown. Places it on the GUI
        :return:
        """
        self.mainCanvas = tk.Canvas(self.mainFrame, bg="white")
        self.mainCanvas.grid(row=0, column=0)

    def initMenus(self):
        """
        Initialises the menus for the application.
        :return:
        """
        #File Menu
        filemenu = tk.Menu(self.menu, tearoff=0)


        openMenu = tk.Menu(filemenu, tearoff=0)
        openMenu.add_command(label="Unchanged", command=lambda: self.invokeFileController(FileMenu.OPEN, IC.ImageColour.UNCHANGED))
        openMenu.add_command(label="Colour", command=lambda: self.invokeFileController(FileMenu.OPEN, IC.ImageColour.COLOUR))
        openMenu.add_command(label="Grayscale", command=lambda: self.invokeFileController(FileMenu.OPEN, IC.ImageColour.GRAYSCALE))
        filemenu.add_cascade(label="Open", menu=openMenu)

        filemenu.add_command(label="Save", command=lambda:self.invokeFileController(FileMenu.SAVE, None))
        filemenu.add_command(label="Close", command=lambda:self.invokeFileController(FileMenu.CLOSE, None))
        self.menu.add_cascade(label="File", menu=filemenu)

        #Algorithm Menu
        algorithmMenu = tk.Menu(self.menu, tearoff=0)
        algorithmMenu.add_command(label="Pixelate", command=lambda:self.invokeAlgorithm(ALG.Algorithm.PIXELATE))
        algorithmMenu.add_command(label="Binary Threshold", command=lambda: self.invokeAlgorithm(ALG.Algorithm.BINARY_THRESHOLD))
        self.menu.add_cascade(label="Algorithms", menu=algorithmMenu)

        #Resize Menu
        resizeMenu = tk.Menu(self.menu, tearoff=0)
        resizeMenu.add_command(label="Resize image", command=lambda:None)
        self.menu.add_cascade(label="Resize", menu=resizeMenu)

        #Settings Menu
        settingsMenu = tk.Menu(self.menu, tearoff=0)
        pixelateMenu = tk.Menu(settingsMenu, tearoff=0)
        pixelateMenu.add_command(label="3", command=lambda:self.changePixelationLevel(3))
        pixelateMenu.add_command(label="5", command=lambda: self.changePixelationLevel(5))
        pixelateMenu.add_command(label="7", command=lambda: self.changePixelationLevel(7))
        pixelateMenu.add_command(label="9", command=lambda: self.changePixelationLevel(9))
        pixelateMenu.add_command(label="11", command=lambda: self.changePixelationLevel(11))
        pixelateMenu.add_command(label="13", command=lambda: self.changePixelationLevel(13))
        pixelateMenu.add_command(label="15", command=lambda: self.changePixelationLevel(15))
        settingsMenu.add_cascade(label="Pixelation", menu=pixelateMenu)
        self.menu.add_cascade(label="Settings", menu=settingsMenu)

    def invokeFileController(self, option, subOption):
        if option == FileMenu.OPEN:
            self.imageArray, self.filename = FMC.openImage(subOption, self.winfo_screenwidth(), self.winfo_screenheight())
            self.imageDimensions = (self.imageArray.shape[1], self.imageArray.shape[0])
            self.updateCanvas()
        elif option == FileMenu.SAVE:
            FMC.saveImage(self.imageArray)
        elif option == FileMenu.CLOSE:
            tk.Tk.destroy(self)
        else:
            print("That option is currently not handled")

    def invokeAlgorithm(self, option):
        if option == ALG.Algorithm.PIXELATE:
            self.imageArray, self.filename = AC.callPixelateAlgorithm(self.filename)
        elif option == ALG.Algorithm.BINARY_THRESHOLD:
            self.imageArray, self.filename = AC.callBinaryThresholdAlgorithm(self.filename)
        else:
            print("That option is currently not handled")
        self.imageDimensions = (self.imageArray.shape[1], self.imageArray.shape[0])
        self.updateCanvas()

    def updateCanvas(self):
        """
        Updates the image on the canvas and resizes it to fit the screen of the device being used.
        :return:
        """
        image = Image.open(self.filename)
        self.canvasImage = ImageTk.PhotoImage(image)
        self.mainCanvas.create_image(0, 0, anchor="nw", image=self.canvasImage)
        self.mainCanvas.config(width=self.imageDimensions[0], height=self.imageDimensions[1])
        print(Globals.pixelationWindowPixels)

    def changePixelationLevel(self, windowSize):
        Globals.pixelationWindowPixels = windowSize



mainLoop = GUI()
mainLoop.mainloop()