from ImageSolve.config import *
from ImageSolve.aboveWidget.doubleAdjustWidget import DoubleAdjustWidget
from ImageSolve.aboveWidget.buttonWidget.openImageWidget import OpenImageWidget


class AboveWidget(QWidget):
    def __init__(self,openFrontImage, openBackImage, sizeFrontAdjust,
                 sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                 lastPage, nextPage, exchangeShowMode, imagePaste, exchangeFrontBack):
        super(AboveWidget, self).__init__()
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignLeft)
        self.openImageWidget = OpenImageWidget(openFrontImage, openBackImage)
        self.sizeWidget = DoubleAdjustWidget(sizeFrontAdjust, sizeBackAdjust)
        self.angleWidget = DoubleAdjustWidget(angleFrontAdjust, angleBackAdjust)
        self.upDownWidget = OpenImageWidget(lastPage, nextPage)
        self.functionWidget = OpenImageWidget(exchangeShowMode, imagePaste)
        self.layout.addWidget(self.openImageWidget)
        self.layout.addWidget(self.sizeWidget)
        self.layout.addWidget(self.angleWidget)
        self.layout.addWidget(self.upDownWidget)
        self.layout.addWidget(self.functionWidget)
        self.layout.addWidget(exchangeFrontBack)
        self.setLayout(self.layout)
