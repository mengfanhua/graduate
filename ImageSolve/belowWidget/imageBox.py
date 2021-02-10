from ImageSolve.config import *
from ImageSolve.algorithms.xyToXY import dx_to_ox, ox_to_dx
from ImageSolve.algorithms.tileCombine import convertNumberToStr, convertStrToNumber
from ImageSolve.belowWidget.imageThread import ImageThread
import math


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
        self.cacheMap = CacheMap()
        self.thread = ImageThread(self.cacheMap)
        self.level = 3

    def set_image(self, img_path):
        """
        open image file
        :param img_path: image file path
        :return:
        """
        self.img = img_path  # 此处需针对不同类型的图片使用不同的加载方法
        self.cacheMap.outlineCachePath = img_path
        if os.path.isfile(img_path):
            self.cacheMap.addOriginMap(img_path)
        self.thread = ImageThread(self.cacheMap)
        self.thread.imageGet.connect(self.paintGet)
        # self.img = Image.open(img_path)
        # self.img = img_path
        self.scaled_img = 1
        self.pointInit()

    def calculate_cache(self):
        x_min = 500 - 768
        y_min = 300 - 512
        x_max = 1536
        y_max = 1024
        x_one, y_one = dx_to_ox(x_min, y_min, self.scale, self.angle, self.point.x(), self.point.y())
        x_two, y_two = dx_to_ox(x_min, y_max, self.scale, self.angle, self.point.x(), self.point.y())
        x_three, y_three = dx_to_ox(x_max, y_min, self.scale, self.angle, self.point.x(), self.point.y())
        x_four, y_four = dx_to_ox(x_max, y_max, self.scale, self.angle, self.point.x(), self.point.y())
        xx_max = max(x_one, x_two, x_three, x_four)
        xx_min = min(x_one, x_two, x_three, x_four)
        yy_max = max(y_one, y_two, y_three, y_four)
        yy_min = min(y_one, y_two, y_three, y_four)
        point_list = []
        for i in range(int(xx_min/256), math.ceil(xx_max/256)+1):
            for j in range(int(yy_min/256), math.ceil(yy_max/256)+1):
                point_list.append((convertNumberToStr(self.level), convertNumberToStr(i), convertNumberToStr(-j)))
        return point_list

    def paintGet(self, cacheMap):
        # self.cacheMap = copy.deepcopy(cacheMap)
        self.repaint()

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
            tempMap = self.cacheMap.pixmap.copy()
            tempList = self.cacheMap.order.copy()
            for i in range(len(tempList)):
                x, y = convertStrToNumber(tempList[i][1]), -convertStrToNumber(tempList[i][2])
                # xx, yy = ox_to_dx(x*256, y*256, self.scale, self.angle, self.point.x(), self.point.y())
                painter.drawPixmap(QPoint(x * 256 + self.point.x(), y * 256 + self.point.y()),
                                   tempMap[tempList[i]])
            painter.end()
            # self.img.crop((left, up, right, down))

    def mouseMoveEvent(self, e):
        """
        mouse move events for the widget
        :param e: QMouseEvent
        :return:
        """
        if self.left_click and self.scaled_img == 1:
            self.end_pos = e.pos() - self.start_pos
            self.point = self.point + self.end_pos
            self.start_pos = e.pos()
            self.repaint()
            self.pointInit()

    def mousePressEvent(self, e):
        """
        mouse press events for the widget
        :param e: QMouseEvent
        :return:
        """
        if e.button() == Qt.LeftButton and self.scaled_img == 1:
            self.left_click = True
            self.start_pos = e.pos()

    def mouseReleaseEvent(self, e):
        """
        mouse release events for the widget
        :param e: QMouseEvent
        :return:
        """
        if e.button() == Qt.LeftButton and self.scaled_img == 1:
            self.left_click = False
            if not self.thread.isRunning():
                self.thread.start()

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

    def pointInit(self):
        point = self.calculate_cache()
        if not self.thread.isRunning():
            self.thread.setPoint(point)
            self.thread.start()
