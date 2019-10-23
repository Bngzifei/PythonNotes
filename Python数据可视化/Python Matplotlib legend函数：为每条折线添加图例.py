# Python Matplotlib legend函数：为每条折线添加图例

"""
对于复式折线图来说，应该为每条折线都添加图例，此时可以通过 legend() 函数来实现。对于该函数可传入两个 list 参数，其中第一个 list 参数（handles 参数）用于引用折线图上的每条折线；第二个 list 参数（labels）代表为每条折线所添加的图例。

下面程序示范了为两条折线添加图例：

"""
import matplotlib.pyplot as plt

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义2个列表分别作为两条折线的Y轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500,58300, 56800, 59500, 62700]
# 指定折线的颜色、线宽和样式
ln1, = plt.plot(x_data, y_data, color = 'red', linewidth = 2.0, linestyle = '--')
ln2, = plt.plot(x_data, y_data2, color = 'blue', linewidth = 3.0, linestyle = '-.')


# 调用legend函数设置图例
plt.legend(handles=[ln2,ln1],labels=["Android基础","Java基础"],loc="lower right")

# 调用show()函数显示图形
plt.show()
