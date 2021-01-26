from ImageSolve.config import *
from ImageSolve.aboveWidget.aboveWidget import AboveWidget
from ImageSolve.belowWidget.belowWidget import BelowWidget


class OneShowWidget(QWidget):
    def __init__(self, openFrontImage, openBackImage, sizeFrontAdjust,
                 sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                 lastPage, nextPage, imageFrontBox, imageBackBox,
                 exchangeShowMode, imagePaste, exchangeFrontBack):
        super(OneShowWidget, self).__init__()
        self.aboveWidget = AboveWidget(openFrontImage, openBackImage, sizeFrontAdjust,
                                       sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                                       lastPage, nextPage, exchangeShowMode, imagePaste,
                                       exchangeFrontBack)
        self.imageBox = BelowWidget(imageFrontBox, imageBackBox)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.aboveWidget)
        self.layout.addWidget(self.imageBox)
        self.setLayout(self.layout)
