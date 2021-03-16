from ImageSolve.mainWindows import MainWindows
from ImageSolve.config import *
from ImageSolve.enterWidget.enterWidget import EnterWidget
from ImageSolve.autoRegistrationWidget.autoRegistrationWidget import AutoRegistrationWidget
from ImageSolve.uploadWidget.uploadWidget import UploadWidget
from ImageSolve.combineWidget.combineWidget import CombineWidget
from ImageSolve.executeWidget.multiImageWidget import MultiImageWidget
from ImageSolve.executeWidget.singleImgeWidget import SingleImageWidget
from ImageSolve.executeWidget.UploadImageWidget import UploadImageWidget
from ImageSolve.proxyWidget.proxyWidget import ProxyWidget
from ImageSolve.properties.proxyInit import *


if __name__ == '__main__':
    proxyInit()
    app = QApplication(sys.argv)
    enter = EnterWidget()
    auto = AutoRegistrationWidget()
    hand = MainWindows()
    upload = UploadWidget()
    combine = CombineWidget()
    oneExecute = MultiImageWidget()
    twoExecute = SingleImageWidget()
    threeExecute = UploadImageWidget()
    proxy1 = ProxyWidget()

    enter.auto.connect(auto.show)
    enter.hand.connect(hand.show)
    enter.upload.connect(upload.show)
    auto.backsignal.connect(enter.show)
    hand.backsignal.connect(enter.show)
    upload.backsignal.connect(enter.show)

    combine.sharepath.connect(upload.set_value)

    hand.combinesignal.connect(combine.come)
    combine.backsignal.connect(hand.show)
    combine.combinesignal.connect(twoExecute.come)
    twoExecute.backsignal.connect(hand.show)

    auto.combinesignal.connect(oneExecute.come)
    oneExecute.backsignal.connect(auto.show)

    upload.combinesignal.connect(threeExecute.come)
    threeExecute.backsignal.connect(upload.show)

    enter.proxy.connect(proxy1.show)
    proxy1.backSignal.connect(enter.show)

    enter.show()
    app.exec_()
