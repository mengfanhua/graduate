from ImageSolve.config import *
from ImageSolve.aboveWidget.doubleAdjustWidget import DoubleAdjustWidget
from ImageSolve.aboveWidget.buttonWidget.openImageWidget import OpenImageWidget


class AboveWidget(QWidget):
    def __init__(self):
        super(AboveWidget, self).__init__()
        self.openImage = OpenImageWidget()
        self.adjust = DoubleAdjustWidget()
        self.exchange = QPushButton("front")
        layout = QHBoxLayout()
        layout.addWidget(self.openImage)
        layout.addWidget(self.adjust)
        layout.addWidget(self.exchange)
        layout.setAlignment(Qt.AlignLeft)
        self.setLayout(layout)
