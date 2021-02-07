from ImageSolve.config import *


class ImageThread(QThread):
    imageGet = pyqtSignal(QPixmap, tuple)

    def __init__(self, cacheMap):
        super(ImageThread, self).__init__()
        self.point = []
        self.cacheMap = cacheMap
        self.flag = 1

    def setPoint(self, point):
        self.point = point.copy()
        self.flag = 1

    def run(self):
        print("成功触发！")
        self.flag = 0
        for i in range(len(self.point)):
            if self.flag == 1:
                break
            map = self.cacheMap.getMap(self.point[i])
            self.imageGet.emit(map, self.point[i])


class TesWidget(QWidget):
    def __init__(self):
        super(TesWidget, self).__init__()
        self.setFixedSize(QSize(500, 300))
        self.cacheMap = CacheMap()
        self.cacheMap.addMap((1, 2, 5), "C:\\Users\\meng\\Desktop\\19892.jpg")
        self.thread = ImageThread(self.cacheMap)
        self.button = QPushButton("触发")
        self.text = QLabel()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)
        self.setLayout(self.layout)
        self.f = 1
        self.button.clicked.connect(self.teext)
        self.thread.imageGet.connect(self.texxt)

    def texxt(self, map, point):
        self.text.setText(str(self.f))
        self.f += 1

    def teext(self):
        while self.thread.isRunning():
            self.thread.stop()
        self.thread.setPoint([(1, 2, 5)])
        self.thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    box = TesWidget()
    box.show()
    app.exec_()