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
    proxyInit()  # 代理初始化，如有代理默认加载
    app = QApplication(sys.argv)  # 主循环
    enter = EnterWidget()  # 入口widget
    auto = AutoRegistrationWidget()  # 自动配准传参界面
    hand = MainWindows()  # 手动配准执行界面
    upload = UploadWidget()  # 上传文件传参界面
    combine = CombineWidget()  # 手动配准传参界面
    oneExecute = MultiImageWidget()  # 自动配准执行界面
    twoExecute = SingleImageWidget()  # 单图配准执行界面
    threeExecute = UploadImageWidget()  # 上传图片执行界面
    proxy1 = ProxyWidget()  # 代理配置界面

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

    enter.show()  # 默认显示入口界面
    app.exec_()
