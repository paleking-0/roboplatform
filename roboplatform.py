import serial
import time
import cv2
import numpy as np
from config import Picamera2


class Robot:
    def __init__(self, resolution: tuple, port: str, debug: bool = False):
        self.resolution = resolution
        self.port = port
        self.debug = debug
        # ser = serial.Serial(self.port, 115200)  # Замените 'COM3' на соответствующий порт

        # self.ser = ser

        if debug:
            self.cam = cv2.VideoCapture(0)
        else:
            picam2 = Picamera2()
            picam2.configure(picam2.create_preview_configuration(raw={"size": (1640, 1232)},
                                                                 main={"format": "RGB888", "size": resolution}))

            picam2.start()
            self.cam = picam2
            # time.sleep(2)

        # time.sleep(2)  # Ждем пару секунд, чтобы порт инициализировался


    def send_to_motor(self, motor, reverse, voltage):
        string_to_send = f"{motor}{reverse}{voltage}\n"
        self.ser.write(string_to_send.encode())

    def get_video_frame(self):
        if self.debug:
            ret, frame = self.cam.read()
            if ret:
                return frame
            else:
                return np.zeros((300, 300, 3), np.uint8)
        else:
            return self.cam.capture_array()

    def end(self):
        self.ser.write("000".encode())
        self.ser.write("100".encode())
        self.ser.close()
        if not self.debug:
            self.cam.stop()
            self.cam.release()
        cv2.destroyAllWindows()



