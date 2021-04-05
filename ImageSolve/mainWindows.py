from ImageSolve.aboveWidget.adjustWidget.adjust import AdjustWidget
from ImageSolve.belowWidget.imageBox import ImageBox
from ImageSolve.modeAdjustWidget.oneShowWidget import OneShowWidget
from ImageSolve.modeAdjustWidget.twoShowWidget import TwoShowWidget
from ImageSolve.aboveWidget.pointShowWidget import PointShowWidget
from ImageSolve.config import *
from ImageSolve.functionWidget.pointWidget import PointWidget
from ImageSolve.algorithms.imageGetThread import ImageGetThread
from ImageSolve.algorithms.getLocation import LocationThread, BDMercatorToLonLatAll


class MainWindows(QWidget):
    backsignal = pyqtSignal()
    combinesignal = pyqtSignal(str, str, list, list, float)

    def __init__(self):
        super(MainWindows, self).__init__()
        self.imageGetThread = ImageGetThread()  # 用于处理网络获取瓦片的子线程
        self.imageGetThread.touch.connect(self.divide_imagebox)
        self.locationThread = LocationThread()  # 用于处理用户输入定位的子线程
        self.locationThread.finish.connect(self.finishEvent)
        self.locationThread1 = LocationThread()  # 同上
        self.locationThread1.finish.connect(self.finishEvent1)
        self.setFixedSize(QSize(1300, 700))
        self.openFrontImage = QPushButton("打开前景图")
        self.openBackImage = QPushButton("打开背景图")
        self.sizeFrontAdjust = AdjustWidget()
        self.sizeBackAdjust = AdjustWidget()
        self.angleFrontAdjust = AdjustWidget()
        self.angleBackAdjust = AdjustWidget()
        self.exchangeBack = QPushButton("front")
        self.pointFrontContent = PointShowWidget()
        self.pointBackContent = PointShowWidget()
        self.lastPage = QLineEdit()
        self.nextPage = QPushButton("城市定位")
        self.exchangeShowMode = QPushButton("切换显示模式")
        self.imagePaste = QPushButton("合成")
        self.imageFrontBox = ImageBox(1, self.imageGetThread)
        self.imageBackBox = ImageBox(2, self.imageGetThread)
        self.radioButton = QRadioButton("加载地图瓦片（百度）")
        self.comeback = QPushButton("返回")
        self.opacity = QSlider(Qt.Vertical)
        self.opacity.setMinimum(0)
        self.opacity.setMaximum(100)
        self.opacity.setSingleStep(1)
        self.opacity.setTickInterval(1)
        self.opacity.setTickPosition(QSlider.TicksAbove)
        self.opacity.valueChanged.connect(self.setOpacity)
        # 同一组件不可同时放置在两个布局中，故复制一份组件，并在监听器中同步操作两个界面
        self.openFrontImage1 = QPushButton("打开前景图")
        self.openBackImage1 = QPushButton("打开背景图")
        self.sizeFrontAdjust1 = AdjustWidget()
        self.sizeBackAdjust1 = AdjustWidget()
        self.angleFrontAdjust1 = AdjustWidget()
        self.angleBackAdjust1 = AdjustWidget()
        self.pointFrontContent1 = PointShowWidget()
        self.pointBackContent1 = PointShowWidget()
        self.lastPage1 = QLineEdit()
        self.nextPage1 = QPushButton("城市定位")
        self.exchangeShowMode1 = QPushButton("切换显示模式")
        self.imagePaste1 = QPushButton("合成")
        self.imageFrontBox1 = ImageBox(3, self.imageGetThread)
        self.imageBackBox1 = ImageBox(4, self.imageGetThread)
        self.radioButton1 = QRadioButton("加载地图瓦片（百度）")
        self.changeLayout = QPushButton("更改布局")
        self.comeback1 = QPushButton("返回")
        self.opacity1 = QSlider(Qt.Horizontal)
        self.opacity1.setMinimum(0)
        self.opacity1.setMaximum(100)
        self.opacity1.setSingleStep(1)
        self.opacity1.setTickInterval(1)
        self.opacity1.setTickPosition(QSlider.TicksAbove)
        self.opacity1.valueChanged.connect(self.setOpacity1)
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackOne)
        self.oneShow = OneShowWidget(self.openFrontImage, self.openBackImage,
                                     self.sizeFrontAdjust, self.sizeBackAdjust,
                                     self.angleFrontAdjust, self.angleBackAdjust,
                                     self.lastPage, self.nextPage, self.imageFrontBox,
                                     self.imageBackBox, self.exchangeShowMode,
                                     self.imagePaste, self.exchangeBack, self.pointFrontContent,
                                     self.pointBackContent, self.radioButton, self.comeback, self.opacity)
        self.twoShow = TwoShowWidget(self.openFrontImage1, self.openBackImage1,
                                     self.sizeFrontAdjust1, self.sizeBackAdjust1,
                                     self.angleFrontAdjust1, self.angleBackAdjust1,
                                     self.lastPage1, self.nextPage1, self.imageFrontBox1,
                                     self.imageBackBox1, self.exchangeShowMode1,
                                     self.imagePaste1, self.pointFrontContent1,
                                     self.pointBackContent1, self.radioButton1, self.changeLayout,
                                     self.comeback1, self.opacity1)
        self.layout.addWidget(self.oneShow)
        self.layout.addWidget(self.twoShow)
        self.setLayout(self.layout)
        self.exchangeShowMode.clicked.connect(self.exchangeMode)
        self.exchangeShowMode1.clicked.connect(self.exchangeMode)
        self.exchangeBack.clicked.connect(self.flag_exchange)
        self.openFrontImage.clicked.connect(self.open_front_image)
        self.openFrontImage1.clicked.connect(self.open_front_image)
        self.openBackImage.clicked.connect(self.open_back_image)
        self.openBackImage1.clicked.connect(self.open_back_image)
        self.sizeFrontAdjust.slider.maxSlider.valueChanged.connect(self.slider_move)
        self.sizeFrontAdjust.slider.minSlider.valueChanged.connect(self.slider_move)
        self.sizeFrontAdjust1.slider.maxSlider.valueChanged.connect(self.slider1_move)
        self.sizeFrontAdjust1.slider.minSlider.valueChanged.connect(self.slider1_move)
        self.sizeBackAdjust.slider.maxSlider.valueChanged.connect(self.slider_move1)
        self.sizeBackAdjust.slider.minSlider.valueChanged.connect(self.slider_move1)
        self.sizeBackAdjust1.slider.maxSlider.valueChanged.connect(self.slider1_move1)
        self.sizeBackAdjust1.slider.minSlider.valueChanged.connect(self.slider1_move1)

        self.angleFrontAdjust.slider.maxSlider.valueChanged.connect(self.slider_angle)
        self.angleFrontAdjust.slider.minSlider.valueChanged.connect(self.slider_angle)
        self.angleFrontAdjust1.slider.maxSlider.valueChanged.connect(self.slider1_angle)
        self.angleFrontAdjust1.slider.minSlider.valueChanged.connect(self.slider1_angle)
        self.angleBackAdjust.slider.maxSlider.valueChanged.connect(self.slider_angle1)
        self.angleBackAdjust.slider.minSlider.valueChanged.connect(self.slider_angle1)
        self.angleBackAdjust1.slider.maxSlider.valueChanged.connect(self.slider1_angle1)
        self.angleBackAdjust1.slider.minSlider.valueChanged.connect(self.slider1_angle1)

        self.radioButton.clicked.connect(self.radioChanged)
        self.radioButton1.clicked.connect(self.radioChanged1)
        self.imageFrontBox.featureSignal.connect(self.addPoint)
        self.imageFrontBox1.featureSignal.connect(self.addPoint)
        self.imageBackBox.featureSignal.connect(self.addPoint1)
        self.imageBackBox1.featureSignal.connect(self.addPoint1)
        # 此处造成前后列表共享，即单独删除某一个页面即可
        self.imageFrontBox.featureList = self.imageFrontBox1.featureList
        self.imageBackBox.featureList = self.imageBackBox1.featureList

        self.changeLayout.clicked.connect(self.change_layout)
        self.nextPage.clicked.connect(self.get_position)
        self.nextPage1.clicked.connect(self.get_position1)
        self.comeback.clicked.connect(self.backEvent)
        self.comeback1.clicked.connect(self.backEvent)
        self.imagePaste.clicked.connect(self.combine)
        self.imagePaste1.clicked.connect(self.combine)
        self.flag_exchange()
        self.flag_exchange()

    def backEvent(self):
        # 返回信号
        self.hide()
        self.backsignal.emit()

    def get_position(self):
        # 在图片已加载且为瓦片格式时触发
        if self.imageBackBox.scaled_img is not None and os.path.isfile(self.imageBackBox.img) is False:
            self.lastPage1.setText(self.lastPage.text())
            self.locationThread.set_city(self.lastPage.text())
            if not self.locationThread.isRunning():
                self.locationThread.start()
            else:
                self.lastPage.setText("访问速度过快！")

    def finishEvent(self, x, y):
        if x == "":
            # 没有查询到结果
            self.lastPage.setText("error")
        else:
            # 通过百度地图与墨卡托坐标转换方法获取瓦片定位
            MClon, MClat = BDMercatorToLonLatAll().convertLonLatToMC(float(x), float(y))
            xx, yy = MClon/math.pow(2, 18-self.imageBackBox.level), MClat/math.pow(2, 18-self.imageBackBox.level)
            self.imageBackBox.point = QPoint(250-int(xx), int(yy)-6)
            self.imageBackBox.pointInit()

    def get_position1(self):
        # 同get_position
        if self.imageBackBox1.scaled_img is not None and os.path.isfile(self.imageBackBox1.img) is False:
            self.lastPage.setText(self.lastPage1.text())
            self.locationThread1.set_city(self.lastPage1.text())
            if not self.locationThread1.isRunning():
                self.locationThread1.start()
            else:
                self.lastPage1.setText("访问速度过快！")

    def finishEvent1(self, x, y):
        # 同finishEvent
        if x == "":
            self.lastPage1.setText("error")
        else:
            MClon, MClat = BDMercatorToLonLatAll().convertLonLatToMC(float(x), float(y))
            xx, yy = MClon / math.pow(2, 18 - self.imageBackBox1.level), MClat / math.pow(2,
                                                                                         18 - self.imageBackBox1.level)
            self.imageBackBox1.point = QPoint(250-int(xx), int(yy)-6)
            self.imageBackBox1.pointInit()

    def divide_imagebox(self, value):
        # 通过预先设定好的编号来确定请求是从哪个界面传出的
        if value == 1:
            self.imageFrontBox.pointInit()
        elif value == 2:
            self.imageBackBox.pointInit()
        elif value == 3:
            self.imageFrontBox1.pointInit()
        else:
            self.imageBackBox1.pointInit()

    def change_layout(self):
        # 更改第二界面布局， 组件不变，但layout改变
        self.twoShow.changeLayout(self.openFrontImage1, self.openBackImage1,
                                  self.sizeFrontAdjust1, self.sizeBackAdjust1,
                                  self.angleFrontAdjust1, self.angleBackAdjust1,
                                  self.lastPage1, self.nextPage1, self.imageFrontBox1,
                                  self.imageBackBox1, self.exchangeShowMode1,
                                  self.imagePaste1, self.pointFrontContent1,
                                  self.pointBackContent1, self.radioButton1, self.changeLayout,
                                  self.comeback1, self.opacity1)
        self.repaint()

    def radioChanged(self):
        # 需同步另一界面的button
        self.radioButton1.setChecked(self.radioButton.isChecked())

    def radioChanged1(self):
        self.radioButton.setChecked(self.radioButton1.isChecked())

    def exchangeMode(self):
        if self.layout.currentIndex() == 0:
            # 将imagebox内的参数共享给另一界面
            self.layout.setCurrentIndex(1)
            self.imageFrontBox1.img = self.imageFrontBox.img
            self.imageFrontBox1.scaled_img = self.imageFrontBox.scaled_img
            self.imageFrontBox1.point = self.imageFrontBox.point
            self.imageFrontBox1.start_pos = self.imageFrontBox.start_pos
            self.imageFrontBox1.end_pos = self.imageFrontBox.end_pos
            self.imageFrontBox1.left_click = self.imageFrontBox.left_click
            self.imageFrontBox1.scale = self.imageFrontBox.scale
            self.imageFrontBox1.angle = self.imageFrontBox.angle
            self.imageFrontBox1.featureList = self.imageFrontBox.featureList
            self.imageFrontBox1.cacheMap = self.imageFrontBox.cacheMap
            self.imageFrontBox1.thread = self.imageFrontBox.thread
            self.imageFrontBox1.level = self.imageFrontBox.level
            self.imageFrontBox1.start_time = self.imageFrontBox.start_time

            self.imageBackBox1.img = self.imageBackBox.img
            self.imageBackBox1.scaled_img = self.imageBackBox.scaled_img
            self.imageBackBox1.point = self.imageBackBox.point
            self.imageBackBox1.start_pos = self.imageBackBox.start_pos
            self.imageBackBox1.end_pos = self.imageBackBox.end_pos
            self.imageBackBox1.left_click = self.imageBackBox.left_click
            self.imageBackBox1.scale = self.imageBackBox.scale
            self.imageBackBox1.angle = self.imageBackBox.angle
            self.imageBackBox1.featureList = self.imageBackBox.featureList
            self.imageBackBox1.cacheMap = self.imageBackBox.cacheMap
            self.imageBackBox1.thread = self.imageBackBox.thread
            self.imageBackBox1.level = self.imageBackBox.level
            self.imageBackBox1.start_time = self.imageBackBox.start_time
            self.repaint()
        else:
            self.layout.setCurrentIndex(0)
            self.imageFrontBox.img = self.imageFrontBox1.img
            self.imageFrontBox.scaled_img = self.imageFrontBox1.scaled_img
            self.imageFrontBox.point = self.imageFrontBox1.point
            self.imageFrontBox.start_pos = self.imageFrontBox1.start_pos
            self.imageFrontBox.end_pos = self.imageFrontBox1.end_pos
            self.imageFrontBox.left_click = self.imageFrontBox1.left_click
            self.imageFrontBox.scale = self.imageFrontBox1.scale
            self.imageFrontBox.angle = self.imageFrontBox1.angle
            self.imageFrontBox.featureList = self.imageFrontBox1.featureList
            self.imageFrontBox.cacheMap = self.imageFrontBox1.cacheMap
            self.imageFrontBox.thread = self.imageFrontBox1.thread
            self.imageFrontBox.level = self.imageFrontBox1.level
            self.imageFrontBox.start_time = self.imageFrontBox1.start_time

            self.imageBackBox.img = self.imageBackBox1.img
            self.imageBackBox.scaled_img = self.imageBackBox1.scaled_img
            self.imageBackBox.point = self.imageBackBox1.point
            self.imageBackBox.start_pos = self.imageBackBox1.start_pos
            self.imageBackBox.end_pos = self.imageBackBox1.end_pos
            self.imageBackBox.left_click = self.imageBackBox1.left_click
            self.imageBackBox.scale = self.imageBackBox1.scale
            self.imageBackBox.angle = self.imageBackBox1.angle
            self.imageBackBox.featureList = self.imageBackBox1.featureList
            self.imageBackBox.cacheMap = self.imageBackBox1.cacheMap
            self.imageBackBox.thread = self.imageBackBox1.thread
            self.imageBackBox.level = self.imageBackBox1.level
            self.imageBackBox.start_time = self.imageBackBox1.start_time
            self.repaint()

    def open_front_image(self):
        """
        select image file and open it
        :return:
        """
        img_name, _ = QFileDialog.getOpenFileName(self, "Open Front Image File", filter="*.jpg;;*.png;;*.jpeg")
        # dir_name = QFileDialog.getExistingDirectory(self, "open a dir")
        if img_name != "":
            self.imageFrontBox.set_image(img_name)
            self.imageFrontBox1.set_image(img_name)

    def open_back_image(self):
        """
        select image file and open it
        :return:
        """
        if self.radioButton.isChecked():
            img_name = QFileDialog.getExistingDirectory(self, "Open a Dir")
        else:
            img_name, _ = QFileDialog.getOpenFileName(self, "Open Back Image File", filter="*.jpg;;*.png;;*.jpeg")
        if img_name != "":
            self.imageBackBox.set_image(img_name)
            self.imageBackBox1.set_image(img_name)

    def slider_move(self):
        """
        used to enlarge image
        :return:
        """
        # 用于前景图缩放比例的计算
        d = float(self.sizeFrontAdjust.slider.maxSlider.value()) / 10
        f = float(self.sizeFrontAdjust.slider.minSlider.value()) / 1000
        self.sizeFrontAdjust1.slider.maxSlider.setValue(self.sizeFrontAdjust.slider.maxSlider.value())
        self.sizeFrontAdjust1.slider.minSlider.setValue(self.sizeFrontAdjust.slider.minSlider.value())
        self.imageFrontBox.scale = d + f
        self.imageFrontBox.pointInit()
        self.update()

    def slider_move1(self):
        """
        used to enlarge image
        :return:
        """
        # 此处分为两种，加载为瓦片则计算层级与放缩比
        if self.imageBackBox.scaled_img and os.path.isfile(self.imageBackBox.img):
            d = float(self.sizeBackAdjust.slider.maxSlider.value()) / 10
            f = float(self.sizeBackAdjust.slider.minSlider.value()) / 1000
            self.sizeBackAdjust1.slider.maxSlider.setValue(self.sizeBackAdjust.slider.maxSlider.value())
            self.sizeBackAdjust1.slider.minSlider.setValue(self.sizeBackAdjust.slider.minSlider.value())
            self.imageBackBox.scale = d + f
        else:
            d = min(max(self.sizeBackAdjust.slider.maxSlider.value(), 3), 19)
            f = float(self.sizeBackAdjust.slider.minSlider.value()) / 100 + 1
            self.sizeBackAdjust1.slider.maxSlider.setValue(self.sizeBackAdjust.slider.maxSlider.value())
            self.sizeBackAdjust1.slider.minSlider.setValue(self.sizeBackAdjust.slider.minSlider.value())
            self.imageBackBox.scale = f
            self.imageBackBox.level = d
        self.imageBackBox.pointInit()
        self.update()

    def slider1_move(self):
        """
        used to enlarge image
        :return:
        """
        d = float(self.sizeFrontAdjust1.slider.maxSlider.value()) / 10
        f = float(self.sizeFrontAdjust1.slider.minSlider.value()) / 1000
        self.sizeFrontAdjust.slider.maxSlider.setValue(self.sizeFrontAdjust1.slider.maxSlider.value())
        self.sizeFrontAdjust.slider.minSlider.setValue(self.sizeFrontAdjust1.slider.minSlider.value())
        self.imageFrontBox1.scale = d + f
        self.imageFrontBox1.pointInit()
        self.update()

    def slider1_move1(self):
        """
        used to enlarge image
        :return:
        """
        if self.imageBackBox1.scaled_img and os.path.isfile(self.imageBackBox1.img):
            d = float(self.sizeBackAdjust1.slider.maxSlider.value()) / 10
            f = float(self.sizeBackAdjust1.slider.minSlider.value()) / 1000
            self.sizeBackAdjust.slider.maxSlider.setValue(self.sizeBackAdjust1.slider.maxSlider.value())
            self.sizeBackAdjust.slider.minSlider.setValue(self.sizeBackAdjust1.slider.minSlider.value())
            self.imageBackBox1.scale = d + f
        else:
            d = min(max(self.sizeBackAdjust1.slider.maxSlider.value(), 3), 19)
            f = float(self.sizeBackAdjust1.slider.minSlider.value()) / 100 + 1
            self.sizeBackAdjust.slider.maxSlider.setValue(self.sizeBackAdjust1.slider.maxSlider.value())
            self.sizeBackAdjust.slider.minSlider.setValue(self.sizeBackAdjust1.slider.minSlider.value())
            self.imageBackBox1.scale = f
            self.imageBackBox1.level = d
        self.imageBackBox1.pointInit()
        self.update()

    def slider_angle(self):
        # 根据计算每个刻度为18度，可满足旋转一周
        if self.imageFrontBox.scaled_img:
            d = float(self.angleFrontAdjust.slider.maxSlider.value() - 1) * 18
            f = float(self.angleFrontAdjust.slider.minSlider.value()) * 0.18
            self.angleFrontAdjust1.slider.maxSlider.setValue(self.angleFrontAdjust.slider.maxSlider.value())
            self.angleFrontAdjust1.slider.minSlider.setValue(self.angleFrontAdjust.slider.minSlider.value())
            self.imageFrontBox.angle = d + f
        self.imageFrontBox.pointInit()
        self.update()

    def slider_angle1(self):
        if self.imageBackBox.scaled_img:
            d = float(self.angleBackAdjust.slider.maxSlider.value() - 1) * 18
            f = float(self.angleBackAdjust.slider.minSlider.value()) * 0.18
            self.angleBackAdjust1.slider.maxSlider.setValue(self.angleBackAdjust.slider.maxSlider.value())
            self.angleBackAdjust1.slider.minSlider.setValue(self.angleBackAdjust.slider.minSlider.value())
            self.imageBackBox.angle = d + f
        self.imageBackBox.pointInit()
        self.update()

    def slider1_angle(self):
        if self.imageFrontBox1.scaled_img:
            d = float(self.angleFrontAdjust1.slider.maxSlider.value() - 1) * 18
            f = float(self.angleFrontAdjust1.slider.minSlider.value()) * 0.18
            self.angleFrontAdjust.slider.maxSlider.setValue(self.angleFrontAdjust1.slider.maxSlider.value())
            self.angleFrontAdjust.slider.minSlider.setValue(self.angleFrontAdjust1.slider.minSlider.value())
            self.imageFrontBox1.angle = d + f
        self.imageFrontBox1.pointInit()
        self.update()

    def slider1_angle1(self):
        if self.imageBackBox1.scaled_img:
            d = float(self.angleBackAdjust1.slider.maxSlider.value() - 1) * 18
            f = float(self.angleBackAdjust1.slider.minSlider.value()) * 0.18
            self.angleBackAdjust.slider.maxSlider.setValue(self.angleBackAdjust1.slider.maxSlider.value())
            self.angleBackAdjust.slider.minSlider.setValue(self.angleBackAdjust1.slider.minSlider.value())
            self.imageBackBox1.angle = d + f
        self.imageBackBox1.pointInit()
        self.update()

    def flag_exchange(self):
        # 重叠样式中，前景图后景图的转换按钮
        if self.exchangeBack.text() == "front":
            self.oneShow.imageBox.layout.setCurrentIndex(1)
            self.oneShow.aboveWidget.sizeWidget.layout.setCurrentIndex(1)
            self.oneShow.aboveWidget.angleWidget.layout.setCurrentIndex(1)
            self.oneShow.aboveWidget.showWidget.layout.setCurrentIndex(1)
            self.exchangeBack.setText("background")
        else:
            self.oneShow.imageBox.layout.setCurrentIndex(0)
            self.oneShow.aboveWidget.sizeWidget.layout.setCurrentIndex(0)
            self.oneShow.aboveWidget.angleWidget.layout.setCurrentIndex(0)
            self.oneShow.aboveWidget.showWidget.layout.setCurrentIndex(0)
            self.exchangeBack.setText("front")
        self.repaint()

    def addPoint(self, point):
        # 触发添加关键点的按钮
        value = self.pointFrontContent.layout.count()
        temp = PointWidget(point, value + 1)
        temp.deletePoint.connect(self.delPoint)
        self.pointFrontContent.layout.addWidget(temp)

        value = self.pointFrontContent1.layout.count()
        temp = PointWidget(point, value + 1)
        temp.deletePoint.connect(self.delPoint)
        self.pointFrontContent1.layout.addWidget(temp)

    def addPoint1(self, point):
        value = self.pointBackContent.layout.count()
        temp = PointWidget(point, value + 1)
        temp.deletePoint.connect(self.delPoint1)
        self.pointBackContent.layout.addWidget(temp)

        value = self.pointBackContent1.layout.count()
        temp = PointWidget(point, value + 1)
        temp.deletePoint.connect(self.delPoint1)
        self.pointBackContent1.layout.addWidget(temp)

    def delPoint(self, value):
        # 触发删除某个关键点
        count = self.pointFrontContent.layout.count()
        for i in range(value, count):
            self.pointFrontContent.layout.itemAt(i).widget().value -= 1
            self.pointFrontContent.layout.itemAt(i).widget().repaint()
        # self.imageFrontBox.featureList.pop(value - 1)
        # 此处有一个关键点：由于两个界面共享featureList，所以只需要删除一次就可以了
        self.pointFrontContent.layout.itemAt(value - 1).widget().deleteLater()

        count = self.pointFrontContent1.layout.count()
        for i in range(value, count):
            self.pointFrontContent1.layout.itemAt(i).widget().value -= 1
            self.pointFrontContent1.layout.itemAt(i).widget().repaint()
        self.imageFrontBox1.featureList.pop(value - 1)
        self.pointFrontContent1.layout.itemAt(value - 1).widget().deleteLater()

        self.repaint()

    def delPoint1(self, value):
        count = self.pointBackContent.layout.count()
        for i in range(value, count):
            self.pointBackContent.layout.itemAt(i).widget().value -= 1
            self.pointBackContent.layout.itemAt(i).widget().repaint()
        # self.imageBackBox.featureList.pop(value - 1)
        self.pointBackContent.layout.itemAt(value - 1).widget().deleteLater()

        count = self.pointBackContent1.layout.count()
        for i in range(value, count):
            self.pointBackContent1.layout.itemAt(i).widget().value -= 1
            self.pointBackContent1.layout.itemAt(i).widget().repaint()
        self.imageBackBox1.featureList.pop(value - 1)
        self.pointBackContent1.layout.itemAt(value - 1).widget().deleteLater()
        self.repaint()

    def combine(self):
        # 触发合成函数
        if len(self.imageFrontBox.featureList) < 3 or len(self.imageBackBox.featureList) < 3:
            QMessageBox.information(self, "error", "至少选择三对标注点！")
        else:
            self.hide()
            self.combinesignal.emit(self.imageFrontBox.img, self.imageBackBox.img,
                                    self.imageFrontBox.featureList, self.imageBackBox.featureList,
                                    self.imageFrontBox.opacity)

    def setOpacity(self):
        self.opacity1.setValue(self.opacity.value())
        value = self.opacity.value()
        self.imageFrontBox.opacity = (100 - value) / 100.0
        self.repaint()

    def setOpacity1(self):
        self.opacity.setValue(self.opacity1.value())
        value = self.opacity1.value()
        self.imageFrontBox1.opacity = (100 - value) / 100.0
        self.repaint()
