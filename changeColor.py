import os
import sys
import time

BASE = os.path.dirname(__file__)

if 'PSMOVEAPI_LIBRARY_PATH' not in os.environ:
    os.environ['PSMOVEAPI_LIBRARY_PATH'] = os.path.join(BASE, 'build')

sys.path.insert(0, os.path.join(BASE, 'bindings', 'python'))

import psmoveapi

class mudarCor(psmoveapi.PSMoveAPI):
    def __init__(self):
        super().__init__()
        self.quit = False

    def on_connect(self, controller: psmoveapi.Controller):
        controller.connection_time = time.time()
        print('Controller connected:', controller, controller.connection_time)

    def on_disconnect(self, controller: psmoveapi.Controller):
        print('Controller disconnected:', controller)
    
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
            controller.color = psmoveapi.RGB(0,0,1)
        if controller.now_pressed(psmoveapi.Button.PS):
            self.quit = True

api = mudarCor()
while not api.quit:
    api.update()