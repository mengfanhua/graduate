# graduate
It's a tool for image registration.(for graduate)


2021年1月23日12:27:05 author：Meng 

设计了基础界面，界面支持打开单个图片，允许前景图与背景图重叠显示，支持前后景切换，支持图片移动和放缩。

算法方面，利用openCV实现了SURF算法，并基于该算法设计局部特征点匹配的加速算法，推导并设计了基于特征点对的图像最小距离拟合方法，并设计了验证性的误差计算方法。
new