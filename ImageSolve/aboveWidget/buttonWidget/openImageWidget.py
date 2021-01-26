from ImageSolve.config import *


class OpenImageWidget(QWidget):
    def __init__(self, frontImage, backImage):
        super(OpenImageWidget, self).__init__()
        layout = QVBoxLayout()
        layout.addWidget(frontImage)
        layout.addWidget(backImage)
        self.setLayout(layout)
