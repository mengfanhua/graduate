# graduate
It's a tool for image registration.(for graduate)


2021年1月23日12:27:05 author：Meng 

设计了基础界面，界面支持打开单个图片，允许前景图与背景图重叠显示，支持前后景切换，支持图片移动和放缩。

算法方面，利用openCV实现了SURF算法，并基于该算法设计局部特征点匹配的加速算法，推导并设计了基于特征点对的图像最小距离拟合方法，并设计了验证性的误差计算方法。


2021年1月24日17:54:13 author：Meng

基于图像拟合方法设计了图层叠加函数，实现了双图像的叠加方法，单图像+瓦片的叠加方法仍在考虑中。

修复了快速SURF算法的部分逻辑错误。

设计了基于多线程的百度地图瓦片的爬虫方法，但尚未测试，且独立于项目，至于后期需不需要整合到项目中看计划需要而改变。

2021年1月26日21:37:19 author：Meng

重构了部分原重叠式UI demo的结构，但尚未测试；接下来尝试构建对比式UI demo的结构；
尝试添加新的组件，尝试修改imagebox的整体结构以完成要求。

2021年1月26日22:12:50 author：Meng

完成了对比式UI的设计组成，尝试主界面的拼装与实现，尝试添加新功能，尝试修改imagebox结构以满足要求。
