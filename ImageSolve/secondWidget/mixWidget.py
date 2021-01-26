from ImageSolve.config import *
from ImageSolve.secondWidget.funWidget.functionWidget import FunctionWidget


class MixWidget(QWidget):
    def __init__(self, openImage, sizeAdjust, angleAdjust, imageBox):
        super(MixWidget, self).__init__()
        self.layout = QHBoxLayout()
        self.functionWidget = FunctionWidget(openImage, sizeAdjust, angleAdjust)
        self.layout.addWidget(imageBox)
        self.layout.addWidget(self.functionWidget)
        self.layout.setStretch(0, 4)
        self.layout.setStretch(1, 1)
        self.setLayout(self.layout)
