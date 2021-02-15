from ImageSolve.config import *
from ImageSolve.aboveWidget.aboveWidget import AboveWidget
from ImageSolve.belowWidget.belowWidget import BelowWidget


class OneShowWidget(QWidget):
    def __init__(self, openFrontImage, openBackImage, sizeFrontAdjust,
                 sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                 lastPage, nextPage, imageFrontBox, imageBackBox,
                 exchangeShowMode, imagePaste, exchangeFrontBack, point1, point2):
        super(OneShowWidget, self).__init__()
        self.aboveWidget = AboveWidget(openFrontImage, openBackImage, sizeFrontAdjust,
                                       sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                                       lastPage, nextPage, exchangeShowMode, imagePaste,
                                       exchangeFrontBack, point1, point2)
        self.imageBox = BelowWidget(imageFrontBox, imageBackBox)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.aboveWidget)
        self.layout.addWidget(self.imageBox)
        self.layout.setStretch(0, 2)
        self.layout.setStretch(1, 7)
        self.setLayout(self.layout)
