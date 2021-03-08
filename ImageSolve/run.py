from ImageSolve.mainWindows import MainWindows
from ImageSolve.config import *
from ImageSolve.enterWidget.enterWidget import EnterWidget
from ImageSolve.autoRegistrationWidget.autoRegistrationWidget import AutoRegistrationWidget
from ImageSolve.uploadWidget.uploadWidget import UploadWidget
from ImageSolve.combineWidget.combineWidget import CombineWidget
from ImageSolve.executeWidget.multiImageWidget import MultiImageWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    enter = EnterWidget()
    auto = AutoRegistrationWidget()
    hand = MainWindows()
    upload = UploadWidget()
    combine = CombineWidget()
    oneExecute = MultiImageWidget()

    enter.auto.connect(auto.show)
    enter.hand.connect(hand.show)
    enter.upload.connect(upload.show)
    auto.backsignal.connect(enter.show)
    hand.backsignal.connect(enter.show)
    upload.backsignal.connect(enter.show)

    hand.combinesignal.connect(combine.come)
    combine.backsignal.connect(hand.show)

    auto.combinesignal.connect(oneExecute.come)
    oneExecute.backsignal.connect(auto.show)


    enter.show()
    app.exec_()
