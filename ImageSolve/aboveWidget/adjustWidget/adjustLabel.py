from ImageSolve.config import *


class LabelAdjustWidget(QWidget):
    def __init__(self):
        super(LabelAdjustWidget, self).__init__()
        label_above = QLabel("粗调:")
        label_below = QLabel("细调:")
        layout = QVBoxLayout()
        layout.addWidget(label_above)
        layout.addWidget(label_below)
        self.setLayout(layout)
