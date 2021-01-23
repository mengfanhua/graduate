from ImageSolve.config import *
from ImageSolve.aboveWidget.aboveWidget import AboveWidget
from ImageSolve.belowWidget.belowWidget import BelowWidget


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Image Viewer")
        self.setFixedSize(1000, 600)
        self.above = AboveWidget()
        self.above.setFixedSize(1000, 100)
        self.above.openImage.setFixedSize(100, 100)
        self.above.adjust.setFixedSize(300, 100)
        self.above.exchange.setFixedSize(100, 30)
        self.below = BelowWidget()
        self.below.resize(500, 300)
        self.below.frontImage.resize(500, 300)
        self.below.backImage.resize(500, 300)
        layout = QVBoxLayout()
        layout.addWidget(self.above)
        layout.addWidget(self.below)
        self.setLayout(layout)
        self.above.adjust.frontAdjust.slider.maxSlider.setValue(5)
        self.above.adjust.frontAdjust.slider.minSlider.setValue(0)
        self.above.adjust.backAdjust.slider.maxSlider.setValue(5)
        self.above.adjust.backAdjust.slider.minSlider.setValue(0)
        self.above.openImage.frontImage.clicked.connect(self.open_front_image)
        self.above.openImage.backImage.clicked.connect(self.open_back_image)
        self.above.adjust.frontAdjust.slider.minSlider.valueChanged.connect(self.slider_move)
        self.above.adjust.frontAdjust.slider.maxSlider.valueChanged.connect(self.slider_move)
        self.above.adjust.backAdjust.slider.minSlider.valueChanged.connect(self.slider_move)
        self.above.adjust.backAdjust.slider.maxSlider.valueChanged.connect(self.slider_move)
        self.above.exchange.clicked.connect(self.flag_exchange)
        self.flag_exchange()
        self.flag_exchange()  # 此处为隐藏bug，未知原因出现拖动bug，需触发两次flag更改才解决

    def open_front_image(self):
        """
        select image file and open it
        :return:
        """
        img_name, _ = QFileDialog.getOpenFileName(self, "Open Front Image File", filter="*.jpg;;*.png;;*.jpeg")
        self.below.frontImage.set_image(img_name)
        """
        d = int(self.below.frontImage.scale * 10)
        f = self.below.frontImage.scale - float(d)/10
        self.above.adjust.frontAdjust.slider.maxSlider.setValue(d)
        self.above.adjust.frontAdjust.slider.minSlider.setValue(int(f * 1000))
        """

    def open_back_image(self):
        """
        select image file and open it
        :return:
        """
        img_name, _ = QFileDialog.getOpenFileName(self, "Open Back Image File", filter="*.jpg;;*.png;;*.jpeg")
        self.below.backImage.set_image(img_name)
        """
        d = int(self.below.backImage.scale * 10)
        f = self.below.backImage.scale - float(d)/10
        self.above.adjust.backAdjust.slider.maxSlider.setValue(d * 10)
        self.above.adjust.backAdjust.slider.minSlider.setValue(int(f * 1000))
        """

    def slider_move(self):
        """
        used to enlarge image
        :return:
        """
        if self.above.exchange.text() == "front":
            d = float(self.above.adjust.frontAdjust.slider.maxSlider.value()) / 10
            f = float(self.above.adjust.frontAdjust.slider.minSlider.value()) / 1000
            self.below.frontImage.scale = d + f
            self.below.frontImage.adjustSize()
            self.update()
        else:
            d = float(self.above.adjust.backAdjust.slider.maxSlider.value()) / 10
            f = float(self.above.adjust.backAdjust.slider.minSlider.value()) / 1000
            self.below.backImage.scale = d + f
            self.below.backImage.adjustSize()
            self.update()

    def flag_exchange(self):
        if self.above.exchange.text() == "front":
            self.below.layout.setCurrentIndex(1)
            self.above.adjust.layout.setCurrentIndex(1)
            self.above.exchange.setText("background")
        else:
            self.below.layout.setCurrentIndex(0)
            self.above.adjust.layout.setCurrentIndex(0)
            self.above.exchange.setText("front")
        self.below.frontImage.flag, self.below.backImage.flag = self.below.backImage.flag, self.below.frontImage.flag
        self.repaint()
