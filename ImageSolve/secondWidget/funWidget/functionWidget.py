from ImageSolve.config import *


class FunctionWidget(QWidget):
    def __init__(self, openImage, sizeAdjust, angleAdjust, point, radio=None):
        super(FunctionWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.layout.addWidget(openImage)
        if radio is not None:
            self.layout.addWidget(radio)
        self.layout.addWidget(sizeAdjust)
        self.layout.addWidget(angleAdjust)
        self.layout.addWidget(point)
        self.setLayout(self.layout)
