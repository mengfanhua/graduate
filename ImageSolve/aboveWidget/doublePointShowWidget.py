from ImageSolve.config import *


class DoublePointShowWidget(QWidget):
    def __init__(self, point1, point2):
        super(DoublePointShowWidget, self).__init__()
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackOne)
        self.layout.addWidget(point1)
        self.layout.addWidget(point2)
        self.setLayout(self.layout)