from ImageUtils import *

def frameProcessing(Frame):
    Result = Frame
    return Result

def videoProcessing(VideoOpenPath, VideoSavePath = None):
    Capture = cv2.VideoCapture(VideoOpenPath)
    Fps = Capture.get(cv2.CAP_PROP_FPS)
    cv2.namedWindow("Input", cv2.WINDOW_GUI_EXPANDED)
    if VideoSavePath is not None:
        Width = int(Capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        Height = int(Capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        Fourcc = int(cv2.VideoWriter_fourcc(*'mp4v'))
        VideoOut = cv2.VideoWriter(VideoSavePath, Fourcc, Fps, (Width, Height), True)
        cv2.namedWindow("Output", cv2.WINDOW_GUI_EXPANDED)
    while Capture.isOpened():
        ret, Frame = Capture.read()
        if ret:
            Output = frameProcessing(Frame)
            cv2.imshow("Input", Frame)
            if VideoSavePath is not None:
                VideoOut.write(Output)
                cv2.imshow("Output", Output)
        else:
            break
        if cv2.waitKey(int(1000.0/Fps)) & 0xFF == ord('q'):
            break
    Capture.release()
    if VideoSavePath is not None:
        VideoOut.release()
    cv2.destroyAllWindows()
