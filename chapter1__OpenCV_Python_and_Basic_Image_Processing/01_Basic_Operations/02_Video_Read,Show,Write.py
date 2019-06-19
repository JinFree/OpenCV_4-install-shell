from Utils import *

VideoPath = "../../Data/Videos/"
Video01 = "solidWhiteRight.mp4"
Video02 = "solidYellowLeft.mp4"
Video03 = "challenge.mp4"

SellectedVideo = Video01

OpenPath = VideoPath + SellectedVideo
WritePath = "Written Video " + SellectedVideo

videoProcessing(OpenPath, WritePath)
