from ImageSolve.mainWindow import MainWindow
from ImageSolve.config import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    box = MainWindow()
    box.show()
    app.exec_()
