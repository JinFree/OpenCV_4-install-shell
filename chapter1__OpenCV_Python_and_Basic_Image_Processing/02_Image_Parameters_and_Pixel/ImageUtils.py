import cv2
import numpy as np


def imageCopy(src):
    return np.copy(src)
    

def getPixel(Image, x, y, c = None):
    return Image[y, x, c]
    
    
def setPixel(Image, value, x, y, c = None):
    Image[y, x, c] = value


def imageParameters(Image, ImageName = "This Image"):
    Height, Width = Image.shape[0], Image.shape[1]
    print("{}.shape is {}".format(ImageName, Image.shape))
    print("{}.shape[0] is height: {}".format(ImageName, Height))
    print("{}.shape[1] is width: {}".format(ImageName, Width))
    print("{}.size is {}".format(ImageName, Image.size))
    print("{}.dtype is {}".format(ImageName, Image.dtype))
    if len(Image.shape) == 2:
        print("{}.shape[2] is Not exist, So channel is 1".format(ImageName))
        print("This image is grayscale.")
        Channel = 1
    else:
        print("{}.shape[2] is channels: {}".format(ImageName, Image.shape[2]))
        print("This image is not grayscale.")
        Channel = 3
    return Height, Width, Channel


def imageRead(OpenPath,
              Flag=cv2.IMREAD_UNCHANGED):
    Image = cv2.imread(OpenPath, Flag)
    if Image is not None:
        print("Image Opened")
        return Image
    else:
        print("Image Not Opened")
        print("Program Abort")
        exit()
        

def imageShow(Image, 
              WindowName = "Image Window", 
              Flag = cv2.WINDOW_GUI_EXPANDED,
              Time = None):
    cv2.namedWindow(WindowName, Flag)
    cv2.imshow(WindowName, Image)
    if Time is None:
        cv2.waitKey()
    else:
        cv2.waitKey(Time)
        

def imageWrite(Image,
               WritePath):
    cv2.imwrite(WritePath, Image)
