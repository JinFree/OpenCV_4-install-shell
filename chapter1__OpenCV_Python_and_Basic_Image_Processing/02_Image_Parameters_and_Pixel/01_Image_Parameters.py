from Utils import *

ImagePath = "../../Data/Images/"
Image01 = "solidWhiteCurve.jpg"
Image02 = "solidYellowCurve.jpg"
Image03 = "whiteCarLaneSwitch.jpg"
Image04 = "solidWhiteRight.jpg"
Image05 = "solidYellowLeft.jpg"
Image06 = "solidYellowCurve2.jpg"
Image07 = "test.png"

SellectedImage = Image01

OpenPath = ImagePath + SellectedImage
WritePath = "Written Image " + SellectedImage

ImageColor = imageRead(OpenPath, cv2.IMREAD_COLOR)
ImageGray = imageRead(OpenPath, cv2.IMREAD_GRAYSCALE)
ImageOrigin = imageRead(OpenPath, cv2.IMREAD_UNCHANGED)

imageParameters(ImageColor, "ImageColor")
imageShow(ImageColor, "ImageColor")

imageParameters(ImageGray, "ImageGray")
imageShow(ImageGray, "ImageGray")

imageParameters(ImageOrigin, "ImageOrigin")
imageShow(ImageOrigin, "ImageOrigin")
