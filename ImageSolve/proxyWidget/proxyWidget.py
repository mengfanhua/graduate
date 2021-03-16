from ImageSolve.config import *
from ImageSolve.autoRegistrationWidget.autoRegistrationWidget import HBoxWidget
from ImageSolve.properties.proxyInit import proxyChange


class ProxyWidget(QWidget):
    backSignal = pyqtSignal()

    def __init__(self):
        super(ProxyWidget, self).__init__()
        self.setFixedSize(QSize(250, 300))
        self.setWindowTitle("配置代理")
        self.bWidget = QWidget()
        self.ly = QVBoxLayout()
        label1 = QLabel("地址：")
        self.edit1 = QLineEdit()
        oneLeft = HBoxWidget(label1, self.edit1, 1, 4)
        label2 = QLabel("端口：")
        self.edit2 = QLineEdit()
        oneRight = HBoxWidget(label2, self.edit2, 1, 1)
        one = HBoxWidget(oneLeft, oneRight, 6, 1)
        label3 = QLabel("账号：")
        self.edit3 = QLineEdit()
        two = HBoxWidget(label3, self.edit3, 1, 4)
        label4 = QLabel("密码：")
        self.edit4 = QLineEdit()
        self.edit4.setEchoMode(QLineEdit.Password)
        three = HBoxWidget(label4, self.edit4, 1, 4)
        self.ly.addWidget(one)
        self.ly.addWidget(two)
        self.ly.addWidget(three)
        self.bWidget.setLayout(self.ly)
        self.radioButton = QRadioButton("不使用代理")
        self.radioButton.setChecked(True)
        self.radioButton1 = QRadioButton("使用http代理")
        self.bWidget.setEnabled(False)
        self.ok = QPushButton("确定")
        self.back = QPushButton("返回")
        four = HBoxWidget(self.ok, self.back, 1, 1)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.radioButton)
        self.layout.addWidget(self.radioButton1)
        self.layout.addWidget(self.bWidget)
        self.layout.addWidget(four)
        self.setLayout(self.layout)
        self.radioButton.clicked.connect(self.changeProxy)
        self.radioButton1.clicked.connect(self.changeProxy1)
        self.ok.clicked.connect(self.updateProxy)
        self.back.clicked.connect(self.backEvent)

    def backEvent(self):
        self.hide()
        self.backSignal.emit()

    def changeProxy(self):
        self.radioButton.setChecked(True)
        self.radioButton1.setChecked(False)
        self.bWidget.setEnabled(False)

    def changeProxy1(self):
        self.radioButton.setChecked(False)
        self.radioButton1.setChecked(True)
        self.bWidget.setEnabled(True)

    def updateProxy(self):
        if self.radioButton.isChecked():
            proxyChange({})
            QMessageBox.information(self, "success", "保存成功！")
            self.hide()
            self.backSignal.emit()
        else:
            if self.edit1.text() == "":
                QMessageBox.information(self, "error", "代理地址不可为空！")
            elif self.edit2.text() == "":
                QMessageBox.information(self, "error", "端口号不可为空！")
            elif self.edit3.text() == "" and self.edit4.text() == "":
                a = {}
                a["http"] = "http://" + self.edit1.text() + ":" + self.edit2.text()
                proxyChange(a)
                QMessageBox.information(self, "success", "保存成功！")
                self.hide()
                self.backSignal.emit()
            elif self.edit3.text() != "" and self.edit4.text() != "":
                a = {}
                a["http"] = "http://" + self.edit3.text() + ":" + self.edit4.text() +\
                            "@" + self.edit1.text() + ":" + self.edit2.text()
                proxyChange(a)
                QMessageBox.information(self, "success", "保存成功！")
                self.hide()
                self.backSignal.emit()
            else:
                QMessageBox.information(self, "error", "账号密码不可单项为空！！")
