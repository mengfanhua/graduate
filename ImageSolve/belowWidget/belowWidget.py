from ImageSolve.config import *


class BelowWidget(QWidget):
    def __init__(self, frontImage, backImage):
        super(BelowWidget, self).__init__()
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackAll)
        self.layout.addWidget(frontImage)
        self.layout.addWidget(backImage)
        self.setLayout(self.layout)
