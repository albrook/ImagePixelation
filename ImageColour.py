from enum import Enum

class ImageColour(Enum):
    """
    An enum that provides options for the colour of which an image will be loaded as.
    """
    UNCHANGED = 1
    COLOUR = 2
    GRAYSCALE = 3