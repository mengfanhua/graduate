from ImageSolve.config import *
from ImageSolve.secondWidget.funWidget.functionWidget import FunctionWidget


class MixHWidget(QWidget):
    def __init__(self, openImage, sizeAdjust, angleAdjust, imageBox, point, radio):
        super(MixHWidget, self).__init__()
        self.layout = QHBoxLayout()
        self.functionWidget = FunctionWidget(openImage, sizeAdjust, angleAdjust, point, radio)
        self.layout.addWidget(imageBox)
        self.layout.addWidget(self.functionWidget)
        self.layout.setStretch(0, 3)
        self.layout.setStretch(1, 1)
        self.setLayout(self.layout)


class MixVWidget(QWidget):
    def __init__(self, openImage, sizeAdjust, angleAdjust, imageBox, point,
                 radio, openBackImage, sizeBackAdjust, angleBackAdjust, imageBackBox, point2):
        super(MixVWidget, self).__init__()
        self.layout = QHBoxLayout()
        self.leftWidget = MixWidget(openImage, sizeAdjust, angleAdjust,imageBox, point, None)
        self.rightWidget = MixWidget(openBackImage, sizeBackAdjust, angleBackAdjust, imageBackBox, point2, radio)
        self.layout.addWidget(self.leftWidget)
        self.layout.addWidget(self.rightWidget)
        self.setLayout(self.layout)


class MixWidget(QWidget):
    def __init__(self,openImage, sizeAdjust, angleAdjust, imageBox, point, radio):
        super(MixWidget, self).__init__()
        self.widget = QWidget()
        self.aboveLayout = QGridLayout()
        self.aboveWidget = QWidget()
        self.ly = QVBoxLayout()
        if radio is not None:
            self.ly.addWidget(openImage)
            self.ly.addWidget(radio)
            self.aboveWidget.setLayout(self.ly)
        else:
            self.ly.addWidget(openImage)
            self.aboveWidget.setLayout(self.ly)
        self.aboveLayout.addWidget(self.aboveWidget, 0, 0)
        self.aboveLayout.addWidget(point, 1, 0)
        self.aboveLayout.addWidget(sizeAdjust, 0, 1)
        self.aboveLayout.addWidget(angleAdjust, 1, 1)
        self.widget.setLayout(self.aboveLayout)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.widget)
        self.layout.addWidget(imageBox)
        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 4)
        self.setLayout(self.layout)

