from ImageSolve.config import *


class HBoxWidget(QWidget):
    def __init__(self, left, right, one, two):
        super(HBoxWidget, self).__init__()
        self.layout = QHBoxLayout()
        self.layout.addWidget(left)
        self.layout.addWidget(right)
        self.layout.setStretch(0, one)
        self.layout.setStretch(1, two)
        self.setLayout(self.layout)


class AutoRegistrationWidget(QWidget):
    backsignal = pyqtSignal()
    combinesignal = pyqtSignal(str, str, str, int)

    def __init__(self):
        super(AutoRegistrationWidget,self).__init__()
        self.setFixedSize(QSize(250, 350))
        self.setWindowTitle("图片自动叠加")
        self.radioButton = QRadioButton("选择文件夹")
        self.label = QLabel("选择第一图片或文件夹：")
        self.edit = QLineEdit()
        self.select = QPushButton("...")
        self.oneWidget = HBoxWidget(self.edit, self.select, 4, 1)
        self.label2 = QLabel("选择第二图片或文件夹：")
        self.edit2 = QLineEdit()
        self.select2 = QPushButton("...")
        self.oneWidget2 = HBoxWidget(self.edit2, self.select2, 4, 1)
        self.label3 = QLabel("选择目的文件夹")
        self.edit3 = QLineEdit()
        self.select3 = QPushButton("...")
        self.oneWidget3 = HBoxWidget(self.edit3, self.select3, 4, 1)
        self.comb = QComboBox()
        self.comb.addItem("快速SURF算法")
        self.comb.addItem("快速SIFT算法")
        self.comb.addItem("sobel+CNN算法")
        self.label4 = QLabel("选择算法：")
        self.oneWidget4 = HBoxWidget(self.label4, self.comb, 1, 4)
        self.ok = QPushButton("确定")
        self.back = QPushButton("返回")
        self.twoWidget = HBoxWidget(self.ok, self.back, 1, 1)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.radioButton)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.oneWidget)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.oneWidget2)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.oneWidget3)
        self.layout.addWidget(self.oneWidget4)
        self.layout.addWidget(self.twoWidget)
        self.setLayout(self.layout)
        self.radioButton.clicked.connect(self.radioChanged)
        self.select.clicked.connect(self.open_image)
        self.select2.clicked.connect(self.open_image1)
        self.select3.clicked.connect(self.open_image2)
        self.back.clicked.connect(self.backEvent)
        self.ok.clicked.connect(self.combine)
        self.edit.setEnabled(False)
        self.edit2.setEnabled(False)
        self.edit3.setEnabled(False)

    def radioChanged(self):
        self.edit.setText("")
        self.edit2.setText("")
        self.edit3.setText("")

    def open_image(self):
        if self.radioButton.isChecked():
            img_name = QFileDialog.getExistingDirectory(self, "Open a Dir")
        else:
            img_name, _ = QFileDialog.getOpenFileName(self, "Open Back Image File", filter="*.jpg;;*.png;;*.jpeg")
        self.edit.setText(img_name)

    def open_image1(self):
        if self.radioButton.isChecked():
            img_name = QFileDialog.getExistingDirectory(self, "Open a Dir")
        else:
            img_name, _ = QFileDialog.getOpenFileName(self, "Open Back Image File", filter="*.jpg;;*.png;;*.jpeg")
        self.edit2.setText(img_name)

    def open_image2(self):
        if self.radioButton.isChecked():
            img_name = QFileDialog.getExistingDirectory(self, "Open a Dir")
        else:
            img_name, _ = QFileDialog.getSaveFileName(self, "Save Image File", filter="*.png")
        self.edit3.setText(img_name)

    def backEvent(self):
        self.hide()
        self.backsignal.emit()

    def combine(self):
        a = self.edit.text()
        b = self.edit2.text()
        c = self.edit3.text()
        d = self.comb.currentIndex()
        if a == "" or b == "" or c == "":
            QMessageBox.information(self, "error", "路径不可为空！")
        else:
            self.hide()
            self.combinesignal.emit(a, b, c, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    box = AutoRegistrationWidget()
    box.show()
    app.exec_()

