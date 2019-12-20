# 调用matplotlib的barh()函数可以生成水平柱状图.barh()函数的用法与bar()的用法基本一样,
# 只是在调用barh()函数时使用y参数传入Y轴数据,使用width参数传入代表条状宽度的数据.

# 例如,如下程序调用barh()函数可以生成水平主状态.barh()函数的用法与bar()的用法基本一样,只是在调用barh()函数
# 时使用y 参数传入Y轴数据,使用width参数传入代表条柱宽度的数据.


# 例如，如下程序调用 barh() 函数生成两组并列的水平柱状图，来展示两套教程历年的销量统计数据：

import matplotlib.pyplot as plt

import numpy as np

# 构建数据
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
bar_width = 0.3


# Y轴数据使用range(len(x_data)),就是0,1,2,...
plt.barh(y=range(len(x_data)), width=y_data, label="Java基础教程",
         color="steelblue", alpha=0.8, height=bar_width)

# Y轴数据使用np.arange(len(x_data)) + bar_width
# 就是bar_width,1+bar_width,2+width...这样就和第一个柱状图并列了

plt.barh(y=np.arange(len(x_data)) + bar_width, width=y_data2,
         label="C语言基础", color="indianred", alpha=0.8, height=bar_width)


# 在柱状图上显示具体数值,ha参数控制水平对齐方式,va控制垂直对齐方式
for y, x in enumerate(y_data):
    plt.text(x + 5000, y - bar_width / 2, "%s" % x, ha="center", va="bottom")

for y, x in enumerate(y_data2):
    plt.text(x + 5000, y + bar_width / 2, "%s" % x, ha="center", va="bottom")


# 为Y轴设置刻度值
plt.yticks(np.arange(len(x_data)) + bar_width / 2, x_data)

# 设置标题
plt.title("Java与C对比")

# 为两条坐标轴设置名称
plt.xlabel("销量")
plt.ylabel("年份")

# 显示图例
plt.legend()
plt.show()
