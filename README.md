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

2021年1月27日14:10:38 author：Meng

修复了由于控件复用产生的界面显示bug，添加了点变换算法的python文件便于调用。


2021年1月31日21:26:24 author：Meng

新增了点击坐标显示区，但信号尚未处理；新增部分监听器实现；测试发现，如使用QPixmap加载图片，则可能出现图片过大导致显存不足越界的情况，若以image型加载，则在拖拉图片时频繁触发重绘函数，导致越界，且加载缓慢。正在思考解决办法。
经计算，地图瓦片数目所占空间远远大于当前我可提供出的磁盘空间，故加载离线地图的方法可能需要改变，即做类似于地图API的加载方式，但如何平衡重绘方法速度和大量加载小图片尚待解决。


2021年2月4日20:58:03 author：Meng

新添加了缓存地图方法类进行地图的动态加载，具体效果如何待测试，且需要子线程的支持，需测试。

2021年2月7日13:24:49 author：Meng

新增图片QPixmap加载的子线程，单测试已通过，从网络获取图片尚未测试，尚未完成与Imagebox的链接与其加速实现。

对于普通图片与瓦片图片的兼容性尚未测试。

2021年2月7日20:34:31 author：Meng

新增瓦片合成与分解算法，初步测试已通过。

2021年2月10日23:25:09 author：Meng

重构了imageBox图片加载的方式，使用imageThread异步加载多个小图片，循环触发，利用cacheMap缓存最活跃图片，并实时更新活跃度。

但经测试发现，在未知的未知会出现崩溃的情况，正在测试解决。

针对图片加载方式，在放缩倍数不为1时，图片出现堆叠或分割的现象，正在寻找误差产生点或逻辑错误点。

2021年2月10日23:34:10 author：Meng

经测试发现，在使用drawPixmap时，无需手动变换坐标，内部函数会自动变换坐标，图片重叠分割问题已解决。

但发现，当缓存数量不足最大值时，会出现空白缓存的情况，故需要根据容纳度动态更改最大缓存，待修改。

2021年2月12日17:25:27 author：Meng

新增了双击点动态触发添加的widget，测试了动态删除功能，待集成。
对于上述缓存问题需要经过其他方法解决，尚无解决办法。

2021年2月15日13:01:32 author：Meng

修改双击触发函数为单击触发，测试了动态添加与删除功能；对于缓存问题添加了动态扩容方法，对多余空间或存在部分问题待解决；
整合部分点显示事件到项目上。

2021年2月15日16:33:06 author：Meng

修复了放缩比例不同时，产生的单击点偏移的bug。

2021年2月17日16:05:04 author：Meng

关联了当前实现的所有的事件触发；添加了加载普通图片与瓦片的切换方法；
完善了用户自主标注功能；对异步加载方法进行部分改进，但仍然存在连接网络加载瓦片时的延迟同步的问题，待修改。