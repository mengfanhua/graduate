import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QStackedLayout, QSlider, QScrollArea, QRadioButton
from PyQt5.Qt import QPixmap, QPoint, Qt, QPainter, QIcon, QColor, QPalette, QPen, QBrush
from PyQt5.QtCore import QSize, pyqtSignal, QThread
import os
from PIL import Image, ImageQt
import requests
import math
from ImageSolve.algorithms.tileCombine import convertNumberToStr, convertStrToNumber
from ImageSolve.algorithms.colorGenerate import ColorTranslate, ColorGenerate


class CacheMap:
    def __init__(self, size=20, cachePath=None):
        self.pixmap = {}
        self.order = []
        self.size = size
        self.outlineCachePath = cachePath
        self.session = requests.session()

    def addOriginMap(self, path, scale=1):
        # 此处专为普通图片设计，用来对大图进行分割，使其避免显存溢出
        self.pixmap[("1", "0", "0")] = QPixmap(path)
        self.order.append(("1", "0", "0"))

    def addMap(self, key, path):
        temp = QPixmap(path)
        self.pixmap[key] = temp
        if len(self.order) == self.size:
            self.pixmap.pop(self.order[0])
            self.order.pop(0)
            self.order.append(key)
        else:
            self.order.append(key)

    def getMap(self, key):
        if key in self.order:
            self.order.pop(self.order.index(key))
            self.order.append(key)
            return self.pixmap[key]
        else:
            paths = self._combinePath(key)
            if paths is None:
                return None
            self.addMap(key, paths)
            return self.pixmap[key]

    def _combinePath(self, key):
        z, x, y = key
        maxs = math.ceil(math.pi * 6378137 / math.pow(2, 26 - int(z)))
        if abs(convertStrToNumber(x)) > maxs or abs(convertStrToNumber(y)) > maxs or\
                int(z) < 3 or int(z) > 19:
            return None
        # 此处添加requests方法，并添加本地缓存
        if os.path.exists(os.path.join(self.outlineCachePath, z, x, y + ".png")):
            return os.path.join(self.outlineCachePath, z, x, y + ".png")
        else:
            try:
                response = self.session.get("https://maponline2.bdimg.com/tile/?qt=vtile&x={}&y={}&z={}&styles=pl&"
                                            "udt=20210119&scaler=1&showtext=0".format(x, y, z))
                if not os.path.exists(os.path.join(self.outlineCachePath, z, x)):
                    os.makedirs(os.path.join(self.outlineCachePath, z, x))
                with open(os.path.join(self.outlineCachePath, z, x, y + ".png"), "wb") as f:
                    f.write(response.content)
                    f.close()
                return os.path.join(self.outlineCachePath, z, x, y + ".png")
            except:
                return None

    def __del__(self):
        self.session.close()


# test
def getValueColor(value):
    return ColorTranslate(ColorGenerate(value))