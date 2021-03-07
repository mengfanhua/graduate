from ImageSolve.config import *
from ImageSolve.secondWidget.mixWidget import MixHWidget
from ImageSolve.secondWidget.bottomWidget import BottomWidget


class HBoxShowWidget(QWidget):
    def __init__(self, openFrontImage, openBackImage, sizeFrontAdjust,
                 sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                 lastPage, nextPage, imageFrontBox, imageBackBox,
                 exchangeShowMode, imagePaste, point1, point2, radio, changeLayout, comeback):
        super(HBoxShowWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.aboveWidget = MixHWidget(openFrontImage, sizeFrontAdjust,
                                     angleFrontAdjust, imageFrontBox, point1, None)
        self.middleWidget = MixHWidget(openBackImage, sizeBackAdjust, angleBackAdjust, imageBackBox, point2, radio)
        self.bottomWidget = BottomWidget(lastPage, nextPage, exchangeShowMode, imagePaste, changeLayout, comeback)
        self.layout.addWidget(self.aboveWidget)
        self.layout.addWidget(self.middleWidget)
        self.layout.addWidget(self.bottomWidget)
        self.layout.setStretch(0, 4)
        self.layout.setStretch(1, 4)
        self.layout.setStretch(2, 1)
        self.setLayout(self.layout)
