##该算法集成两种算法：SURF,SIFT

使用方法：
from imageFastSolve import image_iter_solve

image_iter_solve函数参数及返回值：

参数：\
ori：待配准图像路径；\
des：基准图像路径；\
det：识别器，两种参数的选择：sift或者surf（其他参数会报错）；\
min_xy=None：待配准图像裁剪边的左上角坐标值（迭代使用，无需传值）；\
max_xy=None：待配准图像裁剪边的右下角坐标值（迭代使用，无需传值）；\
min_xy1=None：基准图像裁剪边的左上角坐标值（迭代使用，无需传值）；\
max_xy1=None：基准图像裁剪边的左上角坐标值（迭代使用，无需传值）； \
loss=None：迭代损失。

当使用该函数时，首先要判断要加载的图片为rgb格式，其他格式传入会导致崩溃。

返回值：\
待配准图像标注点的坐标；\
基准图像与之对应的标注点的坐标；\
当前损失。


####注：如果不需要使用迭代式算法，则直接
#####from cvSurfDetect import sift_detect
参数为两个cv.imread()对象与算法选择，与迭代式相同。
#

####依赖的第三方库：python版本：3.7.6
numpy\
opencv-python==3.4.2.16\
opencv-contrib-python==3.4.2.16\
pillow\
以及其他基础包。