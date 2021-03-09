"""
A script that contains an Enum. The Enum describes different ImageColours that can be loaded by GUI.py

Author: Alan Brook
Date: March 2021
"""

from enum import Enum

class ImageColour(Enum):
    """
    An enum that provides options for the colour of which an image will be loaded as.
    """
    UNCHANGED = 1
    COLOUR = 2
    GRAYSCALE = 3