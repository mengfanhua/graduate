from ImageSolve.config import *


class EnterWidget(QWidget):
    auto = pyqtSignal()
    hand = pyqtSignal()
    upload = pyqtSignal()

    def __init__(self):
        super(EnterWidget, self).__init__()
        self.setFixedSize(QSize(250, 300))
        self.setWindowTitle("图片叠加系统")
        pt = QPalette()
        pt.setColor(QPalette.WindowText, QColor("#ff0000"))
        self.autoButton = QPushButton("自动标注")
        self.label = QLabel("    当前自动标注只支持多对两张图\n    片，不支持瓦片！")
        self.label.setPalette(pt)
        self.handButton = QPushButton("手动标注")
        self.label2 = QLabel("    手动标注支持瓦片，但只能单图\n    片合成！")
        self.label2.setPalette(pt)
        self.uploadButton = QPushButton("结果上传")
        self.label3 = QLabel("    选择合成后的文件夹，将图片上\n    传到服务器！")
        self.label3.setPalette(pt)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.autoButton)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.handButton)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.uploadButton)
        self.layout.addWidget(self.label3)
        self.setLayout(self.layout)
        self.autoButton.clicked.connect(self.autoClick)
        self.handButton.clicked.connect(self.handClick)
        self.uploadButton.clicked.connect(self.uploadClick)

    def autoClick(self):
        self.hide()
        self.auto.emit()

    def handClick(self):
        self.hide()
        self.hand.emit()

    def uploadClick(self):
        self.hide()
        self.upload.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    box = EnterWidget()
    box.show()
    app.exec_()
