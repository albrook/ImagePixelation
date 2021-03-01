import tkinter as tk
from PIL import ImageTk,Image, ImageOps
from enum import Enum

import FileMenuController as FMC
import ImageColour as IC

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
        algorithmMenu.add_command(label="Pixelate", command=lambda:None)
        self.menu.add_cascade(label="Algorithms", menu=algorithmMenu)

        #Resize Menu
        resizeMenu = tk.Menu(self.menu, tearoff=0)
        resizeMenu.add_command(label="Resize image", command=lambda:None)
        self.menu.add_cascade(label="Resize", menu=resizeMenu)

    def invokeFileController(self, option, subOption):
        if option == FileMenu.OPEN:
            self.imageArray, self.filename = FMC.openImage(subOption)
            self.updateCanvas()
        elif option == FileMenu.SAVE:
            FMC.saveImage(self.imageArray)
        elif option == FileMenu.CLOSE:
            tk.Tk.destroy(self)
        else:
            print("That option is currently not handled")

    def updateCanvas(self):
        """
        Updates the image on the canvas and resizes it to fit the screen of the device being used.
        :return:
        """
        image = Image.open(self.filename)
        image = ImageOps.fit(image, (self.winfo_screenwidth(), self.winfo_screenheight()))
        self.canvasImage = ImageTk.PhotoImage(image)
        self.mainCanvas.create_image(0, 0, anchor="nw", image=self.canvasImage)
        self.mainCanvas.config(width=self.imageArray.shape[1], height=self.imageArray.shape[0])



mainLoop = GUI()
mainLoop.mainloop()