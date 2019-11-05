"""
使用 Matplotlib 除可以生成包含多条折线的复式折线图之外，它还允许在一张数据图上包含多个子图。

调用 subplot() 函数可以创建一个子图，然后程序就可以在子图上进行绘制。subplot(nrows, ncols, index, **kwargs) 函数的 nrows 参数指定将数据图区域分成多少行；ncols 参数指定将数据图区域分成多少列；index 参数指定获取第几个区域。

subplot() 函数也支持直接传入一个三位数的参数，其中第一位数将作为 nrows 参数；第二位数将作为 ncols 参数；第三位数将作为 index 参数。

下面程序示范了生成多个子图：
"""


import matplotlib.pyplot as plt
import numpy as np


plt.figure()

# 定义从-pi到pi之间的数据,平均取64个数据点
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)

# 将整个figure分成两行两列,第三个参数表示该图形放在第1个网格
plt.subplot(2, 2, 1)
# 绘制正弦曲线
plt.plot()

plt.gca(x_data, np.cos(x_data))
