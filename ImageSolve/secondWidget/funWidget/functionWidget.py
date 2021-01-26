from ImageSolve.config import *


class FunctionWidget(QWidget):
    def __init__(self, openImage, sizeAdjust, angleAdjust):
        super(FunctionWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.layout.addWidget(openImage)
        self.layout.addWidget(sizeAdjust)
        self.layout.addWidget(angleAdjust)
        self.setLayout(self.layout)
