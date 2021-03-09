from ImageSolve.config import *
from ImageSolve.algorithms.updateImage import update_image, validate_key


pause = 0


class UploadImageThread(QThread):
    message = pyqtSignal(str)
    lock = pyqtSignal()
    question = pyqtSignal(str)

    def __init__(self):
        super(UploadImageThread, self).__init__()
        self.img1 = None
        self.key = None

    def set_value(self, img1, key):
        self.img1 = img1
        self.key = key

    def run(self):
        z = os.listdir(self.img1)
        for i in range(len(z)):
            x = os.listdir(os.path.join(self.img1, z[i]))
            for j in range(len(x)):
                y = os.listdir(os.path.join(self.img1, z[i], x[j]))
                for k in range(len(y)):
                    yy = y[k].split(".")[0]
                    self.message.emit("正在验证 " + os.path.join(self.img1, z[i], x[j], y[k]) + " 是否存在。。。\n")
                    if validate_key(z[i], x[j], yy, self.key):
                        self.message.emit("正在上传 " + os.path.join(self.img1, z[i], x[j], y[k]) + "。。。\n")
                        if update_image(os.path.join(self.img1, z[i], x[j], y[k]), z[i], x[j], yy, self.key):
                            self.message.emit(os.path.join(self.img1, z[i], x[j], y[k]) + " 上传成功！\n")
                        else:
                            self.message.emit(os.path.join(self.img1, z[i], x[j], y[k]) + " 上传失败！\n")
                    else:
                        self.question.emit(os.path.join(self.img1, z[i], x[j], y[k]))
                        pause = 0
                        while pause == 0:
                            pass
                        if pause == 1:
                            self.message.emit("用户选择继续。。。\n")
                            self.message.emit("正在上传 " + os.path.join(self.img1, z[i], x[j], y[k]) + "。。。\n")
                            if update_image(os.path.join(self.img1, z[i], x[j], y[k]), z[i], x[j], yy, self.key):
                                self.message.emit(os.path.join(self.img1, z[i], x[j], y[k]) + " 上传成功！\n")
                            else:
                                self.message.emit(os.path.join(self.img1, z[i], x[j], y[k]) + " 上传失败！\n")
                        else:
                            self.message.emit("跳过 " + os.path.join(self.img1, z[i], x[j], y[k]) + " 。\n")
                            continue
                self.message.emit("\n")
        self.message.emit("已完成！\n")
        self.lock.emit()


class UploadImageWidget(QWidget):
    backsignal = pyqtSignal()

    def __init__(self):
        super(UploadImageWidget, self).__init__()
        self.thread = UploadImageThread()
        self.setFixedSize(QSize(250, 300))
        self.content = QPlainTextEdit()
        self.layout = QVBoxLayout()
        self.ok = QPushButton("确定")
        self.layout.addWidget(self.content)
        self.layout.addWidget(self.ok)
        self.layout.setStretch(0, 8)
        self.layout.setStretch(1, 1)
        self.setLayout(self.layout)
        self.content.textChanged.connect(self.valueEvent)
        self.ok.clicked.connect(self.backEvent)
        self.thread.message.connect(self.log_add)
        self.thread.lock.connect(self.finish_log)
        self.thread.question.connect(self.pause_judge)

    def valueEvent(self):
        self.content.verticalScrollBar().setValue(self.content.verticalScrollBar().maximum())

    def come(self, img1, key):
        self.content.setPlainText("初始化。。\n")
        self.ok.setEnabled(False)
        self.thread.set_value(img1, key)
        self.thread.start()
        self.show()

    def backEvent(self):
        self.hide()
        self.backsignal.emit()

    def log_add(self, value):
        self.content.appendPlainText(value)

    def finish_log(self):
        self.ok.setEnabled(True)

    def pause_judge(self, s):
        result = QMessageBox.question(self, "yes or no", s + " 存在或网络异常，是否继续？",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            pause = 1
        else:
            pause = -1
