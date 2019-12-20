"""
可以调用 xlable() 和 ylabel() 函数分别设置 X 轴、Y 轴的名称，也可以通过 title() 函数设置整个数据图的标题，还可以调用 xticks()、yticks() 函数分别改变 X 轴、Y 轴的刻度值（允许使用文本作为刻度值）。
例如,如下程序为数据图添加了名称,标题和坐标轴刻度值:
"""
import matplotlib.pyplot as plt

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

# 定义2个列表分别作为两条折线的Y轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]


# 指定折线的颜色,线宽,和样式
plt.plot(x_data, y_data, color="red", linewidth=2.0,
         linestyle="--", label="Java基础")
plt.plot(x_data, y_data2, color="blue", linewidth=3.0,
         linestyle="-.", label="C基础")

import matplotlib.font_manager as fm
import matplotlib

# 使用Matplotlib的字体管理器加载中文字体
# my_font = fm.FontProperties(fname="D:/git_pro/Python-Notes/Songti.ttc")
font = {'family': 'MicroSoft YaHei',
        'weight': 'bold',
        'size': 10}

matplotlib.rc("font", **font)

# 调用legend函数设置图例
plt.legend(loc="best")
# 设置两条坐标轴的名字
plt.xlabel("年份")
plt.ylabel("教程销量")

# 设置数据图的标题
plt.title("C语言中文网的历年销量")

# 设置Y轴上的刻度值
# 第一个参数是点的位置,第二个参数是点的文字提示
plt.yticks([50000, 70000, 100000], [r"挺好", r"优秀", r"火爆"])

# 调用show()函数显示图形
plt.show()
