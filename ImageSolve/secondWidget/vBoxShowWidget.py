from ImageSolve.config import *
from ImageSolve.secondWidget.mixWidget import MixVWidget
from ImageSolve.secondWidget.bottomWidget import BottomWidget


class VBoxShowWidget(QWidget):
    def __init__(self, openFrontImage, openBackImage, sizeFrontAdjust,
                 sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                 lastPage, nextPage, imageFrontBox, imageBackBox,
                 exchangeShowMode, imagePaste, point1, point2, radio, changeLayout, comeback):
        super(VBoxShowWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.aboveWidget = MixVWidget(openFrontImage, sizeFrontAdjust,
                                     angleFrontAdjust, imageFrontBox, point1, radio,
                                      openBackImage, sizeBackAdjust, angleBackAdjust, imageBackBox, point2)
        self.bottomWidget = BottomWidget(lastPage, nextPage, exchangeShowMode, imagePaste, changeLayout, comeback)
        self.layout.addWidget(self.aboveWidget)
        self.layout.addWidget(self.bottomWidget)
        self.layout.setStretch(0, 9)
        self.layout.setStretch(1, 1)
        self.setLayout(self.layout)
