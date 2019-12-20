"""


Pygal 使用面向对象的方式来生成数据图。使用 Pygal 生成数据图的步骤大致如下：

1、创建 Pygal 数据图对象。Pygal 为不同的数据图提供了不同的类，比如柱状图使用 pygal.Bar 类，饼图使用 pygal.Pie 类，折线图使用 pygal.Line 类，等等。
2、调用数据图对象的 add() 方法添加数据。
3、调用 Config 对象的属性配置数据图。
4、调用数据图对象的 render_to_xxx() 方法将数据图渲染到指定的输出节点（此处的输出节点可以是 PNG 图片、SVG 文件，也可以是其他节点）。

下面通过生成简单的柱状图来演示如何使用 Pygal 生成数据图，该柱状图展示了两种教程从 2011 年到 2017 年的销量统计数据：


"""


import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

# 定义2个列表分别作为两组柱状图的Y轴数据

y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]


# 创建pygal.Bar对象(柱状图)
bar = pygal.Bar()


# 添加两组代表条柱的数据
bar.add("C语言基础", y_data)
bar.add("Python语言基础", y_data2)


# 设置X轴的刻度值
bar.x_labels = x_data

bar.title = "编程教程的历年销量"

# 设置x,y轴的标题
bar.x_title = "年份"
bar.y_title = "销量"

# 指定将数据输出到SVG文件中
bar.render_to_file("fk_books.svg")
