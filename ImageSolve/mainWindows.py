from ImageSolve.aboveWidget.adjustWidget.adjust import AdjustWidget
from ImageSolve.belowWidget.imageBox import ImageBox
from ImageSolve.modeAdjustWidget.oneShowWidget import OneShowWidget
from ImageSolve.modeAdjustWidget.twoShowWidget import TwoShowWidget
from ImageSolve.config import *


class MainWindows(QWidget):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.setFixedSize(QSize(1000, 700))
        self.openFrontImage = QPushButton("打开前景图")
        self.openBackImage = QPushButton("打开背景图")
        self.sizeFrontAdjust = AdjustWidget()
        self.sizeBackAdjust = AdjustWidget()
        self.angleFrontAdjust = AdjustWidget()
        self.angleBackAdjust = AdjustWidget()
        self.exchangeFrontBack = QPushButton("front")
        # self.pointFrontContent
        # self.pointBackContent
        self.lastPage = QPushButton("上一页")
        self.nextPage = QPushButton("下一页")
        self.exchangeShowMode = QPushButton("切换显示模式")
        self.imagePaste = QPushButton("合成")
        self.imageFrontBox = ImageBox()
        self.imageBackBox = ImageBox()
        # 同一组件不可同时放置在两个布局中，故复制一份组件，并在监听器中同步操作两个界面
        self.openFrontImage1 = QPushButton("打开前景图")
        self.openBackImage1 = QPushButton("打开背景图")
        self.sizeFrontAdjust1 = AdjustWidget()
        self.sizeBackAdjust1 = AdjustWidget()
        self.angleFrontAdjust1 = AdjustWidget()
        self.angleBackAdjust1 = AdjustWidget()
        # self.pointFrontContent
        # self.pointBackContent
        self.lastPage1 = QPushButton("上一页")
        self.nextPage1 = QPushButton("下一页")
        self.exchangeShowMode1 = QPushButton("切换显示模式")
        self.imagePaste1 = QPushButton("合成")
        self.imageFrontBox1 = ImageBox()
        self.imageBackBox1 = ImageBox()
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackOne)
        self.oneShow = OneShowWidget(self.openFrontImage, self.openBackImage,
                                     self.sizeFrontAdjust, self.sizeBackAdjust,
                                     self.angleFrontAdjust, self.angleBackAdjust,
                                     self.lastPage, self.nextPage, self.imageFrontBox,
                                     self.imageBackBox, self.exchangeShowMode,
                                     self.imagePaste, self.exchangeFrontBack)
        self.twoShow = TwoShowWidget(self.openFrontImage1, self.openBackImage1,
                                     self.sizeFrontAdjust1, self.sizeBackAdjust1,
                                     self.angleFrontAdjust1, self.angleBackAdjust1,
                                     self.lastPage1, self.nextPage1, self.imageFrontBox1,
                                     self.imageBackBox1, self.exchangeShowMode1,
                                     self.imagePaste1)
        self.layout.addWidget(self.oneShow)
        self.layout.addWidget(self.twoShow)
        self.setLayout(self.layout)
        self.exchangeShowMode.clicked.connect(self.exchangeMode)
        self.exchangeShowMode1.clicked.connect(self.exchangeMode)

    def exchangeMode(self):
        if self.layout.currentIndex() == 0:
            self.layout.setCurrentIndex(1)
        else:
            self.layout.setCurrentIndex(0)
