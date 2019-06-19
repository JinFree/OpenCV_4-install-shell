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

imageShow(ImageColor, "ImageColor, cv2.WINDOW_NORMAL", cv2.WINDOW_NORMAL)
imageShow(ImageColor, "ImageColor, cv2.WINDOW_AUTOSIZE", cv2.WINDOW_AUTOSIZE)
imageShow(ImageColor, "ImageColor, cv2.WINDOW_FREERATIO", cv2.WINDOW_FREERATIO)
imageShow(ImageColor, "ImageColor, cv2.WINDOW_GUI_NORMAL", cv2.WINDOW_GUI_NORMAL)
imageShow(ImageColor, "ImageColor, cv2.WINDOW_GUI_EXPANDED", cv2.WINDOW_GUI_EXPANDED)

imageShow(ImageGray, "ImageGray, 5000ms", Time=5000)

imageWrite(ImageColor, WritePath)
