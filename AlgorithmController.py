import ImportExportImages as IEI
import BinaryThreshold as BT
import PixelationAlgorithm as PA

import Globals

importExportImages = IEI.ImportExport()
GLOBALS = Globals.Globals()

def callPixelateAlgorithm(filename):
    transformedImage = PA.Pixelation(filename)
    return transformedImage, GLOBALS.localSaveFilename

def callBinaryThresholdAlgorithm(filename):
    transformedImage = BT.binary_threshold(filename)
    importExportImages.exportChangedImage(transformedImage)
    return transformedImage, GLOBALS.localSaveFilename