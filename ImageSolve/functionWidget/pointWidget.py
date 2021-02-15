from ImageSolve.config import *


class PointWidget(QWidget):
    deletePoint = pyqtSignal(int)

    def __init__(self, point, value):
        super(PointWidget, self).__init__()
        # self.setFixedHeight(50)
        self.value = value
        self.point = point
        self.label = QLabel(str(self.value) + "." + str((round(point[0]), round(point[1]))))
        pt = QPalette()
        pt.setColor(QPalette.WindowText, QColor(getValueColor(self.value)))
        self.label.setPalette(pt)
        # path will change
        self.deleteButton = QPushButton(icon=QIcon("./Resources/deleteButton.png"))
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setStretch(0, 9)
        self.layout.setStretch(1, 2)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.deleteButton)
        self.setLayout(self.layout)
        self.deleteButton.clicked.connect(self.pushDown)

    def repaint(self):
        super().repaint()
        pt = QPalette()
        pt.setColor(QPalette.WindowText, QColor(getValueColor(self.value)))
        self.label.setPalette(pt)
        self.label.setText(str(self.value) + "." + str((round(self.point[0]),
                                                         round(self.point[1]))))

    def pushDown(self):
        self.deletePoint.emit(self.value)
