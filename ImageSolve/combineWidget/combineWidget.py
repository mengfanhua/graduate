from ImageSolve.config import *
from ImageSolve.autoRegistrationWidget.autoRegistrationWidget import HBoxWidget


class CombineWidget(QWidget):
    backsignal = pyqtSignal()
    combinesignal = pyqtSignal(str, str, list, list, str, int, int)
    sharepath = pyqtSignal(str)

    def __init__(self):
        super(CombineWidget, self).__init__()
        self.img1 = None
        self.img2 = None
        self.featureList1 = None
        self.featureList2 = None
        self.setFixedSize(QSize(250, 300))
        self.setWindowTitle("参数配置")
        self.label = QLabel("请选择目的文件夹：")
        self.edit = QLineEdit()
        self.edit.setEnabled(False)
        self.select = QPushButton("...")
        self.oneWidget = HBoxWidget(self.edit, self.select, 4, 1)
        self.label1 = QLabel("请选择合成瓦片等级范围：（3-19）")
        self.labelspin1 = QLabel("下限：")
        self.spin1 = QSpinBox()
        self.labelspin2 = QLabel("上限：")
        self.spin2 = QSpinBox()
        self.sonWidget1 = HBoxWidget(self.labelspin1, self.spin1, 1, 1)
        self.sonWidget2 = HBoxWidget(self.labelspin2, self.spin2, 1, 1)
        self.sonWidget = HBoxWidget(self.sonWidget1, self.sonWidget2, 1, 1)
        self.spin1.setMinimum(3)
        self.spin1.setMaximum(19)
        self.spin2.setMinimum(3)
        self.spin2.setMaximum(19)
        self.spin1.setValue(3)
        self.spin1.setValue(3)
        self.help = QLabel("地图显示层级为10左右时为最优显示。")
        pt = QPalette()
        pt.setColor(QPalette.WindowText, QColor("#ff0000"))
        self.help.setPalette(pt)
        self.ok = QPushButton("合成")
        self.back = QPushButton("返回")
        self.bottomWidget = HBoxWidget(self.ok, self.back, 1, 1)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.oneWidget)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.sonWidget)
        self.layout.addWidget(self.help)
        self.layout.addWidget(self.bottomWidget)
        self.setLayout(self.layout)
        self.select.clicked.connect(self.open_image)
        self.spin1.valueChanged.connect(self.spinChanged)
        self.spin2.valueChanged.connect(self.spinChanged1)
        self.back.clicked.connect(self.backEvnet)
        self.ok.clicked.connect(self.combine)

    def open_image(self):
        if os.path.isfile(self.img2):
            img_name, _ = QFileDialog.getSaveFileName(self, "Save Image File", filter="*.png")
        else:
            img_name = QFileDialog.getExistingDirectory(self, "Open a Dir")
            self.edit.setText(img_name)

    def spinChanged(self):
        if self.spin1.value() > self.spin2.value():
            self.spin1.setValue(self.spin2.value())

    def spinChanged1(self):
        if self.spin1.value() > self.spin2.value():
            self.spin2.setValue(self.spin1.value())

    def backEvnet(self):
        self.hide()
        self.backsignal.emit()

    def come(self, a, b, c, d):
        self.img1 = a
        self.img2 = b
        self.featureList1 = c
        self.featureList2 = d
        if os.path.isfile(self.img2):
            self.sonWidget.setEnabled(False)
        else:
            self.sonWidget.setEnabled(True)
        self.show()

    def combine(self):
        if self.edit.text() == "":
            QMessageBox.information(self, "error", "路径不可为空！")
        elif os.path.isfile(self.img2):
            a = self.edit.text()
            self.hide()
            self.combinesignal.emit(self.img1, self.img2, self.featureList1, self.featureList2, a, 0, 0)
        else:
            a = self.edit.text()
            asd = os.listdir(a)
            if len(asd) == 0:
                b = self.spin1.value()
                c = self.spin2.value()
                self.sharepath.emit(a)
                self.hide()
                self.combinesignal.emit(self.img1, self.img2, self.featureList1, self.featureList2, a, b, c)
            else:
                QMessageBox.information(self, "error", "该文件夹非空！")
