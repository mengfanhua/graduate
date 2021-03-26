from ImageSolve.config import *


class ImageThread(QThread):
    imageGet = pyqtSignal(CacheMap)

    # 加载瓦片
    def __init__(self, cacheMap):
        super(ImageThread, self).__init__()
        self.point = []
        self.cacheMap = cacheMap
        self.flag = 1

    def setPoint(self, point):
        self.point = point.copy()
        if len(self.point) > self.cacheMap.size:
            self.cacheMap.size = len(self.point) + 10
        self.flag = 1

    def run(self):
        self.flag = 0
        if os.path.isfile(self.cacheMap.outlineCachePath):
            # 此处判断是否为文件，如果为文件则为普通图片，即将所有图片直接加载出来，key值采用倍数法确定
            for i in range(len(self.cacheMap.order)):
                if self.flag == 1:
                    break
                self.cacheMap.getMap(self.cacheMap.order[i])
            self.imageGet.emit(self.cacheMap)
        else:
            for i in range(len(self.point)):
                if self.flag == 1:
                    break
                self.cacheMap.getMap(self.point[i])
            self.imageGet.emit(self.cacheMap)
        # self.cacheMap = ""


class TesWidget(QWidget):
    def __init__(self):
        super(TesWidget, self).__init__()
        self.setFixedSize(QSize(500, 300))
        self.cacheMap = CacheMap(cachePath="C:\\Users\\meng\\Desktop\\19892.jpg")
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
        while not self.thread.isRunning():
            self.thread.quit()
        self.thread.setPoint([(1, 2, 5)])
        self.thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    box = TesWidget()
    box.show()
    app.exec_()