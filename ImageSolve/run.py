from ImageSolve.mainWindows import MainWindows
from ImageSolve.config import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    box = MainWindows()
    box.show()
    app.exec_()
