from ImageSolve.config import *


class ImageBox(QWidget):
    def __init__(self):
        super(ImageBox, self).__init__()
        self.img = None
        self.scaled_img = None
        self.point = QPoint(0, 0)
        self.start_pos = None
        self.end_pos = None
        self.left_click = False
        self.scale = 0.5
        self.flag = 1
        self.op = 1

    def init_ui(self):
        self.setWindowTitle("ImageBox")

    def set_image(self, img_path):
        """
        open image file
        :param img_path: image file path
        :return:
        """
        self.img = QPixmap(img_path)
        self.scaled_img = self.img.scaled(self.size())

    def paintEvent(self, e):
        """
        receive paint events
        :param e: QPaintEvent
        :return:
        """
        if self.scaled_img:
            painter = QPainter()
            painter.begin(self)
            painter.setOpacity(self.op)
            painter.scale(self.scale, self.scale)
            painter.drawPixmap(self.point, self.img)
            painter.end()

    def mouseMoveEvent(self, e):
        """
        mouse move events for the widget
        :param e: QMouseEvent
        :return:
        """
        if self.left_click and self.flag == 1:
            self.end_pos = e.pos() - self.start_pos
            self.point = self.point + self.end_pos
            self.start_pos = e.pos()
            self.repaint()

    def mousePressEvent(self, e):
        """
        mouse press events for the widget
        :param e: QMouseEvent
        :return:
        """
        if e.button() == Qt.LeftButton and self.flag == 1:
            self.left_click = True
            self.start_pos = e.pos()

    def mouseReleaseEvent(self, e):
        """
        mouse release events for the widget
        :param e: QMouseEvent
        :return:
        """
        if e.button() == Qt.LeftButton and self.flag == 1:
            self.left_click = False


class MainDemo(QWidget):
    def __init__(self):
        super(MainDemo, self).__init__()

        self.setWindowTitle("Image Viewer")
        self.setFixedSize(1000, 600)

        self.open_file = QPushButton("Open Image1")
        self.open_file.setToolTip("Open the image1 to view.")
        self.open_file.clicked.connect(self.open_image)
        self.open_file.setFixedSize(150, 30)

        self.open_file1 = QPushButton("Open Image2")
        self.open_file1.setToolTip("Open the image2 to view.")
        self.open_file1.clicked.connect(self.open_image1)
        self.open_file1.setFixedSize(150, 30)

        self.minSlider = QSlider(Qt.Horizontal)
        self.minSlider.setMinimum(0)
        self.minSlider.setMaximum(100)
        self.minSlider.setSingleStep(1)
        self.minSlider.setTickInterval(1)
        self.minSlider.setTickPosition(QSlider.TicksAbove)
        self.minSlider.valueChanged.connect(self.setOpacity)


        self.exchange = QPushButton("front")
        self.exchange.clicked.connect(self.flag_exchange)
        self.exchange.setFixedSize(100, 30)

        w = QWidget(self)
        layout = QHBoxLayout()
        layout.addWidget(self.open_file)
        layout.addWidget(self.open_file1)
        layout.addWidget(self.minSlider)
        layout.addWidget(self.exchange)
        layout.setAlignment(Qt.AlignLeft)
        w.setLayout(layout)
        w.setFixedSize(700, 100)

        k = QWidget()
        k.resize(500, 300)
        self.l = QStackedLayout()
        self.l.setStackingMode(QStackedLayout.StackAll)
        k.setLayout(self.l)

        self.box = ImageBox()
        self.box.resize(500, 300)
        self.box.flag = 1

        self.box1 = ImageBox()
        self.box1.resize(500, 300)
        self.box1.flag = -1

        self.l.addWidget(self.box)
        self.l.addWidget(self.box1)
        self.box.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.box1.setWindowFlags(Qt.WindowStaysOnBottomHint)

        layout = QVBoxLayout()
        layout.addWidget(w)
        layout.addWidget(k)
        self.setLayout(layout)

    def open_image(self):
        """
        select image file and open it
        :return:
        """
        img_name, _ = QFileDialog.getOpenFileName(self, "Open Image1 File", filter="*.jpg;;*.png;;*.jpeg")
        self.box.set_image(img_name)

    def open_image1(self):
        """
        select image file and open it
        :return:
        """
        img_name, _ = QFileDialog.getOpenFileName(self, "Open Image2 File", filter="*.jpg;;*.png;;*.jpeg")
        self.box1.set_image(img_name)

    def large_click(self):
        """
        used to enlarge image
        :return:
        """
        if self.exchange.text() == "front":
            if self.box.scale < 2:
                self.box.scale += 0.1
                self.box.adjustSize()
                self.update()
        else:
            if self.box1.scale < 2:
                self.box1.scale += 0.1
                self.box1.adjustSize()
                self.update()

    def small_click(self):
        """
        used to reduce image
        :return:
        """
        if self.exchange.text() == "front":
            if self.box.scale > 0.1:
                self.box.scale -= 0.1
                self.box.adjustSize()
                self.update()
        else:
            if self.box1.scale > 0.1:
                self.box1.scale -= 0.1
                self.box1.adjustSize()
                self.update()

    def flag_exchange(self):
        if self.exchange.text() == "front":
            self.l.setCurrentIndex(1)
            self.exchange.setText("background")
        else:
            self.l.setCurrentIndex(0)
            self.exchange.setText("front")
        self.box.flag, self.box1.flag = self.box1.flag, self.box.flag
        self.repaint()

    def setOpacity(self):
        value = self.minSlider.value()
        print(value)
        self.box.op = (100 - value) / 100.0
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    box = MainDemo()
    box.show()
    app.exec_()
