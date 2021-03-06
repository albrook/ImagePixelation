import ImportExportImages as IEI
import BinaryThreshold as BT
import PixelationAlgorithm as PA

import Globals

importExportImages = IEI.ImportExport()

def callPixelateAlgorithm(filename):
    transformedImage = PA.Pixelation(filename)
    importExportImages.exportChangedImage(transformedImage)
    return transformedImage, Globals.localSaveFilename

def callBinaryThresholdAlgorithm(filename):
    transformedImage = BT.binary_threshold(filename)
    importExportImages.exportChangedImage(transformedImage)
    return transformedImage, Globals.localSaveFilename