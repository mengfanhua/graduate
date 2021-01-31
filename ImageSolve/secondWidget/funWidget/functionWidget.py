from ImageSolve.config import *


class FunctionWidget(QWidget):
    def __init__(self, openImage, sizeAdjust, angleAdjust, point):
        super(FunctionWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.layout.addWidget(openImage)
        self.layout.addWidget(sizeAdjust)
        self.layout.addWidget(angleAdjust)
        self.layout.addWidget(point)
        self.setLayout(self.layout)
