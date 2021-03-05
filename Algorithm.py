from enum import Enum

class Algorithm(Enum):
    """
    An enum that allows the program to know which algorithm to be run
    """
    PIXELATE = 1
    BINARY_THRESHOLD = 2