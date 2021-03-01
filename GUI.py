import tkinter as tk
from PIL import ImageTk,Image, ImageOps
from enum import Enum

import FileMenuController as FMC
import ImageColour as IC

class FileMenu(Enum):
    OPEN = 1
    SAVE = 2
    CLOSE = 3

class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
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
        self.mainCanvas = tk.Canvas(self.mainFrame, bg="white")
        self.mainCanvas.grid(row=0, column=0)

    def initMenus(self):
        #File Menu
        filemenu = tk.Menu(self.menu, tearoff=0)


        openMenu = tk.Menu(filemenu, tearoff=0)
        openMenu.add_command(label="Unchanged", command=lambda: self.invokeFileController(FileMenu.OPEN, IC.ImageColour.UNCHANGED))
        openMenu.add_command(label="Colour", command=lambda: self.invokeFileController(FileMenu.OPEN, IC.ImageColour.COLOUR))
        openMenu.add_command(label="Grayscale", command=lambda: self.invokeFileController(FileMenu.OPEN, IC.ImageColour.GRAYSCALE))
        filemenu.add_cascade(label="Open", menu=openMenu)

        filemenu.add_command(label="Save", command=lambda:self.invokeFileController(FileMenu.SAVE))
        filemenu.add_command(label="Close", command=lambda:self.invokeFileController(FileMenu.CLOSE))
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
            pass
        elif option == FileMenu.CLOSE:
            tk.Tk.destroy(self)
        else:
            print("That option is currently not handled")

    def updateCanvas(self):
        image = Image.open(self.filename)
        image = ImageOps.fit(image, (self.winfo_screenwidth(), self.winfo_screenheight()))
        self.canvasImage = ImageTk.PhotoImage(image)
        self.mainCanvas.create_image(0, 0, anchor="nw", image=self.canvasImage)
        self.mainCanvas.config(width=self.imageArray.shape[1], height=self.imageArray.shape[0])



mainLoop = GUI()
mainLoop.mainloop()