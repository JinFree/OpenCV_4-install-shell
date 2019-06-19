import cv2
import numpy as np

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
