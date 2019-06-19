from Utils import *

Path = "../../Data/Images/"
Image01 = "solidWhiteCurve.jpg"
Image02 = "solidYellowCurve.jpg"
Image03 = "whiteCarLaneSwitch.jpg"
Image04 = "solidWhiteRight.jpg"
Image05 = "solidYellowLeft.jpg"
Image06 = "solidYellowCurve2.jpg"
Image07 = "test.png"

SellectedImage = Image01

OpenPath = Path + SellectedImage
WritePath = "processed" + SellectedImage

ImageColor = imageRead(OpenPath, cv2.IMREAD_COLOR)
ImageGray = imageRead(OpenPath, cv2.IMREAD_GRAYSCALE)
ImageOrigin = imageRead(OpenPath, cv2.IMREAD_UNCHANGED)

imageShow(Image)
imageWrite(WritePath, Image)
