from ImageSolve.config import *
from ImageSolve.belowWidget.imageBox import ImageBox


class BelowWidget(QWidget):
    def __init__(self):
        super(BelowWidget, self).__init__()
        self.frontImage = ImageBox()
        self.backImage = ImageBox()
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackAll)
        self.layout.addWidget(self.frontImage)
        self.layout.addWidget(self.backImage)
        self.setLayout(self.layout)
        self.backImage.flag = -1
