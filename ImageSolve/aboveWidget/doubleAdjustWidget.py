from ImageSolve.config import *
from ImageSolve.aboveWidget.adjustWidget.adjust import AdjustWidget


class DoubleAdjustWidget(QWidget):
    def __init__(self):
        super(DoubleAdjustWidget, self).__init__()
        self.frontAdjust = AdjustWidget()
        self.backAdjust = AdjustWidget()
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackOne)
        self.frontAdjust.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.backAdjust.setWindowFlags(Qt.WindowStaysOnBottomHint)
        self.layout.addWidget(self.frontAdjust)
        self.layout.addWidget(self.backAdjust)
        self.setLayout(self.layout)

