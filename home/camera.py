import os
import time
import datetime
from home import app

import picamera


def make_image():
    name = datetime.datetime.now().strftime('%d.%m.%y-%H:%M:%S') + '.jpg'
    path = os.path.join(app.static_folder, name)
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        time.sleep(2)
        camera.capture(path)
        camera.stop_preview()
    return name
