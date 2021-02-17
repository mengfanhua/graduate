from ImageSolve.config import *


class OpenImageWidget(QWidget):
    def __init__(self, frontImage, backImage, radio=None):
        super(OpenImageWidget, self).__init__()
        layout = QVBoxLayout()
        layout.addWidget(frontImage)
        layout.addWidget(backImage)
        if radio is not None:
            layout.addWidget(radio)
        self.setLayout(layout)
