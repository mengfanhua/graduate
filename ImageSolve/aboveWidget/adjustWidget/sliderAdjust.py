from ImageSolve.config import *


class SliderAdjustWidget(QWidget):
    def __init__(self):
        super(SliderAdjustWidget, self).__init__()
        self.maxSlider = QSlider(Qt.Horizontal)
        self.maxSlider.setMinimum(1)
        self.maxSlider.setMaximum(20)
        self.maxSlider.setSingleStep(1)
        self.maxSlider.setTickInterval(1)
        self.maxSlider.setTickPosition(QSlider.TicksAbove)

        self.minSlider = QSlider(Qt.Horizontal)
        self.minSlider.setMinimum(0)
        self.minSlider.setMaximum(100)
        self.minSlider.setSingleStep(1)
        self.minSlider.setTickInterval(1)
        self.minSlider.setTickPosition(QSlider.TicksAbove)

        layout = QVBoxLayout()
        layout.addWidget(self.maxSlider)
        layout.addWidget(self.minSlider)
        self.setLayout(layout)
