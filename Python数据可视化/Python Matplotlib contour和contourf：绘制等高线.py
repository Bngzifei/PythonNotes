# Python Matplotlib contour和contourf：绘制等高线


"""
等高线图需要的是三维数据,其中X,Y轴数据决定坐标点,还需要对应的高度数据(相当于Z轴数据)
来决定不同坐标点的高度

有了合适的数据之后,程序调用contour()函数绘制等高线,调用contourf()函数为等高线图填充颜色.

在调用 contour()、contourf() 函数时可以指定如下常用参数：
x：指定 X 轴数据。
y：指定 Y 轴数据。
z：指定 X、Y 坐标对应点的高度数据。
colors：指定不同高度的等高线的颜色。
alpha：指定等高线的透明度。
cmap：指定等高线的颜色映射，即自动使用不同的颜色来区分不同的高度区域。
linewidths：指定等高线的宽度。
linestyles：指定等高线的样式。


下面程序使用contour(),contourf()函数来绘制等高线图:


"""


import matplotlib.pyplot as plt
import numpy as np


delta = 0.025


# 生成代表X轴数据的列表
x = np.arange(-3.0, 3.0, delta)

# 生成代表Y轴数据的列表
y = np.arange(-2.0, 2.0, delta)

# 对x,y数据执行网格化
X, Y = np.meshgrid(x, y)

Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)

# 计算Z轴数据(高度数据)
Z = (Z1 - Z2) * 2

# 为等高线图填充颜色,16指定将等高线分为几部分
plt.contourf(x, y, Z, 16, alpha=0.75, cmap="rainbow")  # 使用颜色映射来区分不同高度的区域

# 绘制等高线
C = plt.contour(x, y, Z, 16, colors="black",  # 指定等高线的颜色
                linewidth=0.5)  # 指定等高线的线宽


# 绘制等高线数据
plt.clabel(C, inline=True, fontsize=10)


# 去除坐标轴
plt.xticks(())
plt.yticks(())


# 设置标题
plt.title("等高线图")

# 为两条坐标轴设置名称
plt.xlabel("纬度")
plt.ylabel("经度")


plt.show()
