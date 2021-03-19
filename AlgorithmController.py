"""
A script that is used as a controller for GUI.py.
This controller contains methods associated with calling algorithms to transform images.

Author: Alan Brook
Date: March 2021
"""

import ImportExportImages as IEI
import BinaryThreshold as BT
import PixelationAlgorithm as PA

import Globals

importExportImages = IEI.ImportExport()

def callPixelateAlgorithm(filename):
    """
    Given a filename, passes the filename onto the relevant algorithm from PixelationAlgorithm.py (pixelation) saves the transformed image and
    returns the transformed image and the local save of the transformed image.
    :param filename (String): The directory of the image ot be transformed
    :return (List, String): The transformed image, and the directory of the local save file.
    """
    transformedImage = PA.pixelation(filename)
    importExportImages.exportChangedImage(transformedImage)
    return transformedImage, Globals.localSaveFilename

def callPixelateAndShrinkAlgorithm(filename):
    """
    Given a filename, passes the filename onto the relevant algorithm from PixelationAlgorithm.py (pixelateAndShrink), saves the transformed image and
    returns the transformed image and the local save of the transformed image.
    :param filename (String): The directory of the image ot be transformed
    :return (List, String): The transformed image, and the directory of the local save file.
    """
    transformedImage = PA.pixelateAndShrink(filename)
    importExportImages.exportChangedImage(transformedImage)
    return transformedImage, Globals.localSaveFilename

def callBinaryThresholdAlgorithm(filename):
    """
    Given a filename, passes the filename onto the relevant algorithm (BinaryThreshold.py), saves the transformed image and
    returns the transformed image and the local save of the transformed image.
    :param filename (String): The directory of the image ot be transformed
    :return (List, String): The transformed image, and the directory of the local save file.
    """
    transformedImage = BT.binary_threshold(filename)
    importExportImages.exportChangedImage(transformedImage)
    return transformedImage, Globals.localSaveFilename