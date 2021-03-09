from ImageSolve.config import *
from ImageSolve.autoRegistrationWidget.autoRegistrationWidget import HBoxWidget


class UploadWidget(QWidget):
    backsignal = pyqtSignal()

    def __init__(self):
        super(UploadWidget, self).__init__()
        self.setFixedSize(QSize(300, 300))
        self.setWindowTitle("图片上传")
        self.label = QLabel("选择文件夹：")
        self.edit = QLineEdit()
        self.edit.setEnabled(False)
        self.select = QPushButton("...")
        self.label1 = QLabel("账号：")
        self.username = QLineEdit()
        self.label2 = QLabel("密码：")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.label3 = QLabel("注：本账号密码只用于生成密钥，请尽量复杂！")
        self.ok = QPushButton("确定")
        self.back = QPushButton("返回")
        pt = QPalette()
        pt.setColor(QPalette.WindowText, QColor("#ff0000"))
        self.label3.setPalette(pt)
        self.oneWidget = HBoxWidget(self.edit, self.select, 4, 1)
        self.twoWidget = HBoxWidget(self.label1, self.username, 1, 4)
        self.threeWidget = HBoxWidget(self.label2, self.password, 1, 4)
        self.fourWidget = HBoxWidget(self.ok, self.back, 1, 1)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.oneWidget)
        self.layout.addWidget(self.twoWidget)
        self.layout.addWidget(self.threeWidget)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.fourWidget)
        self.setLayout(self.layout)
        self.select.clicked.connect(self.open_image)
        self.back.clicked.connect(self.comeback)

    def open_image(self):
        img_name = QFileDialog.getExistingDirectory(self, "Open a Dir")
        self.edit.setText(img_name)

    def comeback(self):
        self.hide()
        self.backsignal.emit()

    def set_value(self, s):
        self.edit.setText(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    box = UploadWidget()
    box.show()
    app.exec_()

