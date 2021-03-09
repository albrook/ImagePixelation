"""
A script that contains an Enum. The Enum describes different algorithms that are present and can be used in GUI.py

Author: Alan Brook
Date: March 2021
"""

from enum import Enum

class Algorithm(Enum):
    """
    An enum that allows the program to know which algorithm to be run
    """
    PIXELATE = 1
    BINARY_THRESHOLD = 2