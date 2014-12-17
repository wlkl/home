import os
import time
import datetime
from home import app

import picamera


def make_image():
    name = os.path.join(app.static_folder, datetime.datetime.now().strftime('%d.%m.%y-%H:%M:%S') + '.jpg')
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        time.sleep(2)
        camera.capture(name)
        camera.stop_preview()
    return name
