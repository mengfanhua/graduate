from ImageSolve.config import *
from ImageSolve.algorithms.imageFastSolve import image_iter_solve
from ImageSolve.algorithms.imageTranslate import image_translate
from ImageSolve.algorithms.combineImage import combine_image


class MultiImageThread(QThread):
    message = pyqtSignal(str)
    lock = pyqtSignal()

    def __init__(self):
        super(MultiImageThread, self).__init__()
        self.img1 = None
        self.img2 = None
        self.img3 = None

    def set_value(self, img1, img2, img3):
        self.img1 = img1
        self.img2 = img2
        self.img3 = img3

    def run(self):
        if os.path.isfile(self.img1):
            self.message.emit("正在生成标注点。。。\n")
            ori_key, des_key, _ = image_iter_solve(self.img1, self.img2)
            self.message.emit("生成完成，正在进行匹配计算。。。\n")
            alpha, k, dx, dy = image_translate(ori_key, des_key)
            self.message.emit("匹配完成，正在进行合成。。。\n")
            a, _ = combine_image(self.img1, self.img2, k, alpha, dx, dy)
            a.save(self.img3)
            self.message.emit("合成完成。\n\n")
        else:
            imgList1 = os.listdir(self.img1)
            imgList2 = os.listdir(self.img2)
            for i in range(len(imgList1)):
                self.message.emit("正在验证第" + str(i+1) + "组标注点。。。\n")
                if imgList1[i] in imgList2:
                    self.message.emit("正在生成第" + str(i + 1) + "组标注点。。。\n")
                    ori_key, des_key, _ = image_iter_solve(self.img1 + imgList1[i], self.img2 + imgList1[i])
                    self.message.emit("正在计算第" + str(i + 1) + "组标注点偏移。。。\n")
                    alpha, k, dx, dy = image_translate(ori_key, des_key)
                    self.message.emit("正在合成第" + str(i + 1) + "组图片。。。\n")
                    a, _ = combine_image(self.img1 + imgList1[i], self.img2 + imgList1[i], k, alpha, dx, dy)
                    a.save(self.img3 + imgList1[i])
                    self.message.emit("第" + str(i + 1) + "组图片合成完成。\n\n")
                else:
                    self.message.emit("没有与第" + str(i + 1) + "组相同名称的图片。\n\n")
                    continue
        self.lock.emit()


class MultiImageWidget(QWidget):
    backsignal = pyqtSignal()

    def __init__(self):
        super(MultiImageWidget, self).__init__()
        self.thread = MultiImageThread()
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

    def valueEvent(self):
        self.content.verticalScrollBar().setValue(self.content.verticalScrollBar().maximum())

    def come(self, img1, img2, img3):
        self.content.setPlainText("初始化。。\n")
        self.ok.setEnabled(False)
        self.thread.set_value(img1, img2, img3)
        self.thread.start()
        self.show()

    def backEvent(self):
        self.hide()
        self.backsignal.emit()

    def log_add(self, value):
        self.content.appendPlainText(value)

    def finish_log(self):
        self.ok.setEnabled(True)