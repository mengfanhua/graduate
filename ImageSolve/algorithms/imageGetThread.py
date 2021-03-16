from PyQt5.QtCore import pyqtSignal, QThread
import os
import requests
from ImageSolve.properties.proxyInit import *


toDoList = list()
containItem = set()


class ImageGetThread(QThread):
    touch = pyqtSignal(int)

    def __init__(self):
        super(ImageGetThread, self).__init__()
        self.session = requests.session()
        self.tryCount = 0

    def run(self):
        while len(toDoList) != 0:
            temp = toDoList[0]
            # temp为元组，格式为（z，x，y，value，outlinecachepath）
            try:
                response = self.session.get("http://maponline2.bdimg.com/tile/?qt=vtile&x={}&y={}&z={}&styles=pl&"
                                            "udt=20210119&scaler=1&showtext=0".format(temp[1], temp[2], temp[0]),
                                            timeout=10, proxies=proxy)
                if not os.path.exists(os.path.join(temp[4], temp[0], temp[1])):
                    os.makedirs(os.path.join(temp[4], temp[0], temp[1]))
                with open(os.path.join(temp[4], temp[0], temp[1], temp[2] + ".png"), "wb") as f:
                    f.write(response.content)
                    f.close()
                self.touch.emit(temp[3])
                toDoList.pop(0)
                containItem.remove(temp)
            except:
                print("yichang!")
                self.tryCount += 1
                if self.tryCount >= 3:
                    toDoList.pop(0)
                    containItem.remove(temp)
                    self.tryCount = 0
                else:
                    pass

    def __del__(self):
        self.session.close()
