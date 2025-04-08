import psmoveapi
import cv2 as cv
import numpy as np

class Controller(psmoveapi.PSMoveAPI):
    def __init__(self):
        super().__init__()
        self.quit = False

    def on_connect(self, controller: psmoveapi.Controller):
        print("Connected Controller")
        controller.color = psmoveapi.RGB(0.5,0,1)
    def on_disconnect(self, controller):
        pass
    
    def on_update(self, controller: psmoveapi.Controller):
        if controller.now_pressed(psmoveapi.Button.TRIANGLE):
            controller.color = psmoveapi.RGB(0.25,0.88,0.67)
        if controller.now_pressed(psmoveapi.Button.CIRCLE):
            controller.color = psmoveapi.RGB(1,0.4,0.4)
        if controller.now_pressed(psmoveapi.Button.CROSS):
            controller.color = psmoveapi.RGB(0.48,0.69,0.9)
        if controller.now_pressed(psmoveapi.Button.SQUARE):
            controller.color = psmoveapi.RGB(1,0.41,0.97)
        if controller.now_pressed(psmoveapi.Button.MOVE):
            controller.color = psmoveapi.RGB(0.55,0.74,0.25)
        if controller.now_pressed(psmoveapi.Button.PS):
            self.quit = True

def changeSaturation(frame, saturation):
    framehsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV).astype("float32")
    (h, s, v) = cv.split(framehsv)
    s = s*saturation
    s = np.clip(s,0,255)
    framehsv = cv.merge([h,s,v])
    return cv.cvtColor(framehsv.astype("uint8"), cv.COLOR_HSV2BGR)

api = Controller()

cap = cv.VideoCapture(0)

while not api.quit:
    api.update()
    ret, frame = cap.read()

    frame = cv.convertScaleAbs(frame, alpha=0.3)

    cv.imshow("colmeia", frame)
    if ord('q') == cv.waitKey(20):
        break

cv.destroyAllWindows()