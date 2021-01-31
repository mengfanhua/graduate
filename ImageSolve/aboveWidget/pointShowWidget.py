from ImageSolve.config import *


class PointShowWidget(QWidget):
    def __init__(self):
        super(PointShowWidget, self).__init__()
        self.layout = QVBoxLayout()
        ly = QVBoxLayout()
        self.area = QScrollArea()
        self.layout.setAlignment(Qt.AlignTop)
        self.area.setLayout(self.layout)
        ly.addWidget(self.area)
        self.setLayout(ly)
