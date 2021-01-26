from ImageSolve.config import *
from ImageSolve.aboveWidget.adjustWidget.adjust import AdjustWidget


class DoubleAdjustWidget(QWidget):
    def __init__(self, frontAdjust, backAdjust):
        super(DoubleAdjustWidget, self).__init__()
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackOne)
        frontAdjust.setWindowFlags(Qt.WindowStaysOnTopHint)
        backAdjust.setWindowFlags(Qt.WindowStaysOnBottomHint)
        self.layout.addWidget(frontAdjust)
        self.layout.addWidget(backAdjust)
        self.setLayout(self.layout)
