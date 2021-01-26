from ImageSolve.aboveWidget.adjustWidget.adjust import AdjustWidget
from ImageSolve.belowWidget.imageBox import ImageBox
from ImageSolve.modeAdjustWidget.oneShowWidget import OneShowWidget
from ImageSolve.modeAdjustWidget.twoShowWidget import TwoShowWidget
from ImageSolve.config import *


class MainWindows(QWidget):
    def __init__(self):
        super(MainWindows, self).__init__()
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
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackOne)
        self.oneShow = OneShowWidget(self.openFrontImage, self.openBackImage,
                                     self.sizeFrontAdjust, self.sizeBackAdjust,
                                     self.angleFrontAdjust, self.angleBackAdjust,
                                     self.lastPage, self.nextPage, self.imageFrontBox,
                                     self.imageBackBox, self.exchangeShowMode,
                                     self.imagePaste, self.exchangeFrontBack)
        self.twoShow = TwoShowWidget(self.openFrontImage, self.openBackImage,
                                     self.sizeFrontAdjust, self.sizeBackAdjust,
                                     self.angleFrontAdjust, self.angleBackAdjust,
                                     self.lastPage, self.nextPage, self.imageFrontBox,
                                     self.imageBackBox, self.exchangeShowMode,
                                     self.imagePaste)
        self.layout.addWidget(self.oneShow)
        self.layout.addWidget(self.twoShow)
        self.setLayout(self.layout)
