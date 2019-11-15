"""
凭借着NumPy和SciPy提供的高阶数组和矩阵操作,Python成为科学计算应用的主流语言.
NumPy实现了多维同质数组和矩阵,这些数据结构不但能处理数字,还能存放其他由用户自定义的记录.
通过NumPy,用户能对这些数据结构里的元素进行高效的操作.

SciPy是基于NumPy的另一个库,它提供了很多跟科学计算有关的算法,专为线性代数,数值积分和统计学
而设计.SciPy的高效和可靠性归功于器背后的C和Fortran代码,而这些跟计算有关的部分都源自于Netlib
库.换句话说,SciPy把基于C和Fortran的工业级数学计算功能用交互式且高度抽象的Python包装起来,
让科学家如鱼得水.
"""


# 对numpy.ndarray的行和列进行基本操作

import numpy
a = numpy.arange(12)
print(a)  # [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(type(a))  # <class 'numpy.ndarray'>
print(a.shape)  # (12,)
a.shape = 3,4
print(a.shape)  # (3, 4)

print(a)

"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

print(a[2])  # [ 8  9 10 11]
print(a[2][1])  # 9

"""

注意:NumPy和SciPy的安装可能会比较费劲.SciPy.org建议找一个科学计算Python
的分发渠道帮忙,比如Anacoda,Enthought Canopy,WinPython,等等.

常见的GNU/Linux版本的用户应该可以在他们自己的包管理系统中找到NumPy和SciPy.
例如,在Debian或者Ubuntu上面,用户可以通过下面的命令一键安装:
	$ sudo apt-get install python-numpy python-scipy


NumPy和SciPy都是异常强大的库,也是其他一些很有用的工具的基石.Pandas和Blaze
数据分析库就以它们为基础,提供了高效的且能存储非数值类数据的数组类型,
和读写常见数据格式(例如csv,xls,SQL转储和HDF5)的功能.



	在介绍完扁平序列(包括标准数组和NumPy数组)之后,让我们把目光投向Python中可以取代
	列表的另外一种数据结构:队列

"""