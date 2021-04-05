from ImageSolve.config import *
from ImageSolve.algorithms.imageTranslate import image_translate
from ImageSolve.algorithms.combineImage import combine_image
from ImageSolve.algorithms.exchangeType import exchangeType, exchangeTile
from ImageSolve.algorithms.tileCombine import combineTileToImage, divideImageToTile


class SingleImageThread(QThread):
    message = pyqtSignal(str)
    lock = pyqtSignal()

    def __init__(self):
        super(SingleImageThread, self).__init__()
        self.ori_key = None
        self.des_key = None
        self.img1 = None
        self.img2 = None
        self.output = None
        self.below = None
        self.above = None
        self.opacity = None

    def set_value(self, img1, img2, ori_key, des_key, output, below, above, opacity):
        self.ori_key = ori_key.copy()
        self.des_key = des_key.copy()
        self.img1 = img1
        self.img2 = img2
        self.output = output
        self.below = below
        self.above = above
        self.opacity = opacity

    def run(self):
        ori_key = exchangeType(self.ori_key)
        if os.path.isfile(self.img2):
            self.message.emit("正在转换标注点。。。\n")
            des_key = exchangeType(self.des_key)
            self.message.emit("正在进行参数计算。。。\n")
            alpha, k, dx, dy = image_translate(ori_key, des_key)
            self.message.emit("正在合成。。。\n")
            a, _ = combine_image(self.img1, self.img2, k, alpha, dx, dy, self.opacity)
            self.message.emit("图片合成完毕。\n\n")
            a.save(self.output)
        else:
            front_image = Image.open(self.img1)
            fronts = front_image.convert("RGBA")
            for i in range(self.below, self.above + 1):
                self.message.emit("正在转换第" + str(i) + "层级的标注点。。。\n")
                des_key = exchangeTile(self.des_key, i)
                self.message.emit("正在计算第" + str(i) + "层级的参数。。。\n")
                alpha, k, dx, dy = image_translate(ori_key, des_key)
                f_x, f_y = fronts.size
                front = fronts.resize((int(f_x * k), int(f_y * k)), Image.ANTIALIAS)  # 此处放缩尽可能放大，否则会损失精度，必要时可放大背景图
                front = front.rotate(-alpha, expand=True)
                nf_x, nf_y = front.size
                off_x = k * math.cos(math.radians(alpha)) * f_x / 2 - k * math.sin(math.radians(alpha)) * f_y / 2 - nf_x / 2
                off_y = k * math.sin(math.radians(alpha)) * f_x / 2 + k * math.cos(math.radians(alpha)) * f_y / 2 - nf_y / 2
                min_x = int((-off_x + dx)/256)-1
                min_y = int((-off_y + dy)/256)-1
                max_x = math.ceil((nf_x - off_x + dx)/256)+2
                max_y = math.ceil((nf_y - off_y + dy)/256)+2
                self.message.emit("正在合成第" + str(i) + "层级待配准瓦片。。。\n")
                des_image = combineTileToImage(i, min_x, min_y, max_x-min_x+1,
                                               max_y-min_y+1, self.img2)
                self.message.emit("正在合成。。。\n")
                a, _ = combine_image(self.img1, des_image, k, alpha, dx - min_x * 256,
                                     dy - min_y * 256, self.opacity)
                self.message.emit("合成完成，正在分割瓦片并保存。。。\n")
                divideImageToTile(a, i, min_x, min_y, self.output)
                self.message.emit("第" + str(i) + "层级瓦片处理完成。\n\n")
        self.lock.emit()


class SingleImageWidget(QWidget):
    backsignal = pyqtSignal()

    def __init__(self):
        super(SingleImageWidget, self).__init__()
        self.thread = SingleImageThread()
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

    def valueEvent(self):
        self.content.verticalScrollBar().setValue(self.content.verticalScrollBar().maximum())

    def come(self, img1, img2, fe1, fe2, a, b, c, o):
        self.content.setPlainText("初始化。。\n")
        self.ok.setEnabled(False)
        self.thread.set_value(img1, img2, fe1, fe2, a, b, c, o)
        self.thread.start()
        self.show()

    def backEvent(self):
        self.hide()
        self.backsignal.emit()

    def log_add(self, value):
        self.content.appendPlainText(value)

    def finish_log(self):
        self.ok.setEnabled(True)

