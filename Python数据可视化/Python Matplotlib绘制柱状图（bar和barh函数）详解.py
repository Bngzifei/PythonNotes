# Python Matplotlib绘制柱状图（bar和barh函数）详解
# 下面程序使用柱状图来展示《C语言基础》和《Java基础》两套教程历年的销量数据。


import matplotlib.pyplot as plt
import numpy as np


# 构建数据
x_data = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
bar_width = 0.3

# 绘图
# plt.bar(x=x_data, height=y_data, label="C语言基础", color="steelblue", alpha=0.8)
# plt.bar(x=x_data, height=y_data2, label="Java语言基础",
#         color="indianred", alpha=0.8)


# 将X轴数据改为使用range(len(x_data)),就是0,1,2...
plt.bar(x=range(len(x_data)), height=y_data, label="C语言基础",
        color="steelblue", alpha=0.8, width=bar_width)


# 将X轴数据改为使用np.arange(len(x_data))+bar_width,
# 就是bar_width,1+bar_width,2+bar_width...这样就和第一个柱状图并列了.
plt.bar(x=np.arange(len(x_data)) + bar_width, height=y_data2,
        label="Java基础", color="indianred", alpha=0.8, width=bar_width
        )


# 在柱状图上显示具体数值,ha参数控制水平对齐方式,va控制垂直对齐方式
for x, y in enumerate(y_data):
    plt.text(x, y + 100, "%s" % y, ha="center", va="bottom")


for x, y in enumerate(y_data2):
    plt.text(x, y + 100, "%s" % y, ha="center", va="top")


# 设置标题
plt.title("C与Android图书对比")
# 为两条坐标轴设置名称
plt.xlabel("年份")
plt.ylabel("销量")


# 显示图例
plt.legend()
plt.show()
