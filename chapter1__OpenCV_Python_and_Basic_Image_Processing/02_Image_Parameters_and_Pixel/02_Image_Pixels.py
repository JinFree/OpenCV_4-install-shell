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

x, y = 100, 200
PixelValue = getPixel(ImageColor, x, y)
print("{}: Pixel values in {}, {}: {}".format("ImageColor", x, y, PixelValue))

PixelValue_b = getPixel(ImageColor, x, y, 0)
PixelValue_g = getPixel(ImageColor, x, y, 1)
PixelValue_r = getPixel(ImageColor, x, y, 2)
print("{}: Pixel values in {}, {}: b={}, g={}, r={}".format("ImageColor", x, y, PixelValue_b, PixelValue_g, PixelValue_r))
imageShow(ImageColor, "ImageColor")

PixelValue = getPixel(ImageGray, x, y)
print("{}: Pixel values in {}, {}: {}".format("ImageGray", x, y, PixelValue))
imageShow(ImageGray, "ImageGray")


#PPT 31 page in edit
