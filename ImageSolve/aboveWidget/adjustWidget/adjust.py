from ImageSolve.aboveWidget.adjustWidget.sliderAdjust import SliderAdjustWidget
from ImageSolve.aboveWidget.adjustWidget.adjustLabel import LabelAdjustWidget
from ImageSolve.config import *


class AdjustWidget(QWidget):
    def __init__(self):
        super(AdjustWidget, self).__init__()
        label = LabelAdjustWidget()
        self.slider = SliderAdjustWidget()
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.slider)
        self.setLayout(layout)
