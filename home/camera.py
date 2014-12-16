import time, datetime
import picamera

def make_image():
    name = datetime.datetime.strftime('%d.%m.%y-%H:%M:%S') + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution(1024, 768)
        camera.start_preview()
        time.sleep(2)
        camera.capture(name)
        camera.stop_preview()
    return name
