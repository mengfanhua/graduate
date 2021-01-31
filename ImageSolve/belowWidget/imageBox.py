from ImageSolve.config import *
from PIL import Image, ImageQt
from ImageSolve.algorithms.xyToXY import dx_to_ox


class ImageBox(QWidget):
    featureSignal = pyqtSignal(tuple)

    def __init__(self):
        super(ImageBox, self).__init__()
        self.img = None
        self.scaled_img = None
        self.point = QPoint(0, 0)
        self.start_pos = None
        self.end_pos = None
        self.left_click = False
        self.scale = 1
        self.angle = 0
        self.featureList = []

    def set_image(self, img_path):
        """
        open image file
        :param img_path: image file path
        :return:
        """
        # self.img = QPixmap(img_path)  # 此处需更改为加载PIL，然后在绘图时执行转换
        self.img = Image.open(img_path)
        self.scaled_img = 1

    def paintEvent(self, e):
        """
        receive paint events
        :param e: QPaintEvent
        :return:
        """
        if self.scaled_img:
            # 此处需更改成分块加载，避免出现显存不足越界的情况
            # 在绘图之前，需将特征点首先绘制，以用来锚定图片位置
            # timg = ImageQt.toqpixmap(self.img)
            painter = QPainter()
            painter.begin(self)
            painter.translate(0, 0)
            painter.scale(self.scale, self.scale)
            painter.rotate(self.angle)
            # 下面绘图部分需根据具体图片大小进行分割，然后分块加载，至于起止点需通过计算得出
            # painter.drawPixmap(self.point, timg)
            # painter.drawPixmap(self.point, self.img)
            painter.end()
            # self.img.crop((left, up, right, down))

    def mouseMoveEvent(self, e):
        """
        mouse move events for the widget
        :param e: QMouseEvent
        :return:
        """
        if self.left_click:
            self.end_pos = e.pos() - self.start_pos
            self.point = self.point + self.end_pos
            self.start_pos = e.pos()
            self.repaint()

    def mousePressEvent(self, e):
        """
        mouse press events for the widget
        :param e: QMouseEvent
        :return:
        """
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self.start_pos = e.pos()

    def mouseReleaseEvent(self, e):
        """
        mouse release events for the widget
        :param e: QMouseEvent
        :return:
        """
        if e.button() == Qt.LeftButton:
            self.left_click = False

    def mouseDoubleClickEvent(self, e):
        # 此处需要添加记录特征点模块，需要测试
        if e.button() == Qt.LeftButton and self.scaled_img == 1:
            x, y = e.pos().x(), e.pos().y()
            dx, dy = self.point.x(), self.point.y()
            # 此处为x', y'点，需通过反向计算得到图上对应的原点
            ox, oy = dx_to_ox(x, y, self.scale, self.angle, dx, dy)
            self.featureList.append((ox, oy))
            self.repaint()
            self.featureSignal.emit((ox, oy))
