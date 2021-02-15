from ImageSolve.config import *


class PointShowWidget(QWidget):
    def __init__(self):
        super(PointShowWidget, self).__init__()
        self.layout = QVBoxLayout()
        ly = QVBoxLayout()
        self.area = QScrollArea()
        self.layout.setAlignment(Qt.AlignTop)
        ly.addWidget(self.area)
        self.content = QWidget()
        self.layout.setSpacing(0)
        # self.content.setFixedWidth()
        self.content.setLayout(self.layout)
        self.area.setWidget(self.content)
        self.area.setWidgetResizable(True)
        self.setLayout(ly)
        self.area.verticalScrollBar().rangeChanged.connect(self.get_last)

    def get_last(self):
        self.area.verticalScrollBar().setValue(self.area.verticalScrollBar().maximum())
