###CNNMatcher使用方法

输入及返回值：

参数：\
img1：待配准图像；\
img2：基准图像。

返回值：\
待配准图像标注点的坐标；\
基准图像与之对应的标注点的坐标。

#
####注：在使用前根据执行文件路径修改libAlg.cnn_feature.py与libAlg.model.py中关于模型路径的部分，修改为从执行文件路径开始的完整相对路径。
#
####依赖的第三方库：python版本：3.7.6
torch\
torchvision\
scipy==1.2.1\
numpy\
pillow\
opencv-python==3.4.2.16\
opencv-contrib-python==3.4.2.16\
scikit-image\
以及其他基础包。