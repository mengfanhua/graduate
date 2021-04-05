from ImageSolve.config import *
from ImageSolve.secondWidget.hBoxShowWidget import HBoxShowWidget
from ImageSolve.secondWidget.vBoxShowWidget import VBoxShowWidget


class TwoShowWidget(QWidget):
    def __init__(self, openFrontImage, openBackImage, sizeFrontAdjust,
                 sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                 lastPage, nextPage, imageFrontBox, imageBackBox,
                 exchangeShowMode, imagePaste, point1, point2, radio,
                 changeLayout, comeback, opacity):
        super(TwoShowWidget, self).__init__()
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackOne)
        self.value = 0
        self.content = HBoxShowWidget(openFrontImage, openBackImage, sizeFrontAdjust,
                                      sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                                      lastPage, nextPage, imageFrontBox, imageBackBox,
                                      exchangeShowMode, imagePaste, point1, point2, radio,
                                      changeLayout, comeback, opacity)
        self.layout.addWidget(self.content)
        self.layout.setCurrentIndex(0)
        self.setLayout(self.layout)

    def changeLayout(self, openFrontImage, openBackImage, sizeFrontAdjust,
                 sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                 lastPage, nextPage, imageFrontBox, imageBackBox,
                 exchangeShowMode, imagePaste, point1, point2, radio,
                     changeLayout, comeback, opacity):
        if self.value == 0:
            self.value += 1
            content = VBoxShowWidget(openFrontImage, openBackImage, sizeFrontAdjust,
                                          sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                                          lastPage, nextPage, imageFrontBox, imageBackBox,
                                          exchangeShowMode, imagePaste, point1, point2, radio,
                                     changeLayout, comeback, opacity)
            self.layout.addWidget(content)
            self.layout.setCurrentIndex(1)
            self.repaint()
        else:
            if self.layout.currentIndex() == 1:
                content = HBoxShowWidget(openFrontImage, openBackImage, sizeFrontAdjust,
                                              sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                                              lastPage, nextPage, imageFrontBox, imageBackBox,
                                              exchangeShowMode, imagePaste, point1, point2, radio, changeLayout,
                                         comeback, opacity)
                self.layout.itemAt(0).widget().deleteLater()
                self.layout.insertWidget(0, content)
                self.layout.setCurrentIndex(0)
                self.repaint()
            else:
                content = VBoxShowWidget(openFrontImage, openBackImage, sizeFrontAdjust,
                                         sizeBackAdjust, angleFrontAdjust, angleBackAdjust,
                                         lastPage, nextPage, imageFrontBox, imageBackBox,
                                         exchangeShowMode, imagePaste, point1, point2, radio,
                                         changeLayout, comeback, opacity)
                self.layout.itemAt(1).widget().deleteLater()
                self.layout.insertWidget(1, content)
                self.layout.setCurrentIndex(1)
                self.repaint()
