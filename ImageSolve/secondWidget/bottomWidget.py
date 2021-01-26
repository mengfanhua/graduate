from ImageSolve.config import *


class BottomWidget(QWidget):
    def __init__(self, lastPage, nextPage, exchangeShowMode, imagePaste):
        super(BottomWidget, self).__init__()
        self.layout = QHBoxLayout()
        self.layout.addWidget(lastPage)
        self.layout.addWidget(nextPage)
        self.layout.addWidget(exchangeShowMode)
        self.layout.addWidget(imagePaste)
        self.layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.layout)
