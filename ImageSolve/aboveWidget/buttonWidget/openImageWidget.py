from ImageSolve.config import *


class OpenImageWidget(QWidget):
    def __init__(self):
        super(OpenImageWidget, self).__init__()
        self.frontImage = QPushButton("选择前景图")
        self.backImage = QPushButton("选择后景图")
        layout = QVBoxLayout()
        layout.addWidget(self.frontImage)
        layout.addWidget(self.backImage)
        self.setLayout(layout)
