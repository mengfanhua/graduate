from ImageSolve.config import *
from ImageSolve.functionWidget.pointWidget import PointWidget


class widget(QWidget):
    def __init__(self):
        super(widget, self).__init__()
        self.asd = PointWidget((1, 2, 3), 1)
        self.zxc = PointWidget((1, 5, 3), 2)
        self.radioButton = QRadioButton("click")
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.asd)
        self.layout.addWidget(self.zxc)
        self.layout.addWidget(self.radioButton)
        self.setLayout(self.layout)
        self.asd.deletePoint.connect(self.delWidget)
        self.zxc.deletePoint.connect(self.delWidget)
        self.radioButton.clicked.connect(self.tett)

    def tett(self):
        print(self.radioButton.isChecked())
        self.radioButton.setChecked(False)

    # 测试layout对组件的删除作用
    def delWidget(self, value):
        count = self.layout.count()
        for i in range(value, count):
            self.layout.itemAt(i).widget().value -= 1
            self.layout.itemAt(i).widget().repaint()
        self.layout.itemAt(value - 1).widget().deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    box = widget()
    box.show()
    app.exec_()
