from ImageSolve.config import *
from ImageSolve.algorithms.colorGenerate import ColorGenerate
from ImageSolve.algorithms.colorGenerate import ColorTranslate


class widget(QWidget):
    def __init__(self):
        super(widget, self).__init__()
        self.setFixedHeight(700)
        self.button = QPushButton("添加")
        self.value = 0
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.tett)

    def tett(self):
        num = self.value % 16 + 14
        pt = QPalette()
        color = ColorTranslate(ColorGenerate(num*3.3))
        print(color)
        pt.setColor(QPalette.WindowText, QColor(color))
        label = QLabel("hello!")
        label.setPalette(pt)
        self.layout.addWidget(label)
        self.value += 1
        label.repaint()

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
