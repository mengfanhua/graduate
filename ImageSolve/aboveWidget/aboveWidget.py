from ImageSolve.config import *
from ImageSolve.aboveWidget.doubleAdjustWidget import DoubleAdjustWidget
from ImageSolve.aboveWidget.buttonWidget.openImageWidget import OpenImageWidget
from ImageSolve.aboveWidget.doublePointShowWidget import DoublePointShowWidget


class AboveWidget(QWidget):
    def __init__(self,openFrontImage, openBackImage, sizeFrontAdjust,
                 sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                 lastPage, nextPage, exchangeShowMode, imagePaste, exchangeFrontBack,
                 point1, point2, radio, comeback, opacity):
        super(AboveWidget, self).__init__()
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignLeft)
        self.openImageWidget = OpenImageWidget(openFrontImage, openBackImage, radio)
        self.sizeWidget = DoubleAdjustWidget(sizeFrontAdjust, sizeBackAdjust)
        self.angleWidget = DoubleAdjustWidget(angleFrontAdjust, angleBackAdjust)
        self.upDownWidget = OpenImageWidget(lastPage, nextPage)
        self.functionWidget = OpenImageWidget(exchangeShowMode, imagePaste)
        self.showWidget = DoublePointShowWidget(point1, point2)
        self.functionTwoWidget = OpenImageWidget(exchangeFrontBack, comeback)
        self.layout.addWidget(self.openImageWidget)
        self.layout.addWidget(self.sizeWidget)
        self.layout.addWidget(self.angleWidget)
        self.layout.addWidget(self.showWidget)
        self.layout.addWidget(opacity)
        self.layout.addWidget(self.upDownWidget)
        self.layout.addWidget(self.functionWidget)
        self.layout.addWidget(self.functionTwoWidget)
        self.layout.setStretch(0, 2)
        self.layout.setStretch(1, 4)
        self.layout.setStretch(2, 4)
        self.layout.setStretch(3, 8)
        self.layout.setStretch(4, 1)
        self.layout.setStretch(5, 2)
        self.layout.setStretch(6, 2)
        self.layout.setStretch(7, 2)
        self.setLayout(self.layout)
