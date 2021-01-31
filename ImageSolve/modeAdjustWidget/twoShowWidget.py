from ImageSolve.config import *
from ImageSolve.secondWidget.mixWidget import MixWidget
from ImageSolve.secondWidget.bottomWidget import BottomWidget


class TwoShowWidget(QWidget):
    def __init__(self, openFrontImage, openBackImage, sizeFrontAdjust,
                 sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                 lastPage, nextPage, imageFrontBox, imageBackBox,
                 exchangeShowMode, imagePaste, point1, point2):
        super(TwoShowWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.aboveWidget = MixWidget(openFrontImage, sizeFrontAdjust,
                                     angleFrontAdjust, imageFrontBox, point1)
        self.middleWidget = MixWidget(openBackImage, sizeBackAdjust, angleBackAdjust, imageBackBox, point2)
        self.bottomWidget = BottomWidget(lastPage, nextPage, exchangeShowMode, imagePaste)
        self.layout.addWidget(self.aboveWidget)
        self.layout.addWidget(self.middleWidget)
        self.layout.addWidget(self.bottomWidget)
        self.layout.setStretch(0, 4)
        self.layout.setStretch(1, 4)
        self.layout.setStretch(2, 1)
        self.setLayout(self.layout)
