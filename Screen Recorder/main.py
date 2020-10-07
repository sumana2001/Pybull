import sys
import glob
from threading import Thread
import shutil
import os
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from pyautogui import screenshot
import cv2

class App(QWidget, Thread):
    def __init__(self):

        super().__init__()
        self.title = 'Py_Recorder'
        self.count = 0
        self.status = True

        Thread.__init__(self)
        self.daemon = Thread(target=self.start_recording, name="start_recording")
        self.daemon.setDaemon(True)
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(10, 10, 500, 50)


        button = QPushButton('Start Screen Recording', self)
        button.setToolTip('Click here to start recording')
        button.move(10, 10)
        button.clicked.connect(self.start_threading)


        button = QPushButton('Take a Snap', self)
        button.setToolTip('Click here to take screenshot')
        button.move(190, 10)
        button.clicked.connect(self.take_screenshot)


        button = QPushButton('Stop Screen Recording', self)
        button.setToolTip('Click here to stop recording')
        button.move(320, 10)
        button.clicked.connect(self.stop_recording)
        self.show()

    def start_recording(self):
        print("Inside start recording")
        while self.status:
            self.count += 1
            if not os.path.isdir("screenshots"):
                os.mkdir("screenshots")
            else:
                filename = "screenshots/" + str(self.count) + ".jpg"
                screenshot(filename)

    @pyqtSlot()
    def start_threading(self):
        print("Inside start threading")
        self.daemon.start()

    @pyqtSlot()
    def stop_recording(self):
        print('Stop Button has been pressed')
        try:
            img_array = []
            self.status = False
            for filename in glob.glob('screenshots/*.jpg'):
                img = cv2.imread(filename)
                height, width, layers = img.shape
                size = (width, height)
                img_array.append(img)
            out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
            for i in range(len(img_array)):
                out.write(img_array[i])
            out.release()
            shutil.rmtree('screenshots')
            exit()
        except:
            exit()

    def take_screenshot(self):
        """Take screen shot and store to a directory"""
        if not os.path.isdir("screenshot"):
            os.mkdir("screenshot")
        filename = "screenshot/" + str(time.time()) + ".jpg"
        screenshot(filename)
        img = cv2.imread(filename)
        cv2.imshow("Screenshot", img)
        cv2.waitKey(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())