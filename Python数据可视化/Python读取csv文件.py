"""

Python读取csv文件

前面程序展示的数据都是直接通过程序给出的，但实际应用可能需要展示不同来源（比如文件、网络）、不同格式（比如 csv、JSON）的数据，这些数据可能有部分是损坏的，因此程序需要对这些数据进行处理。

csv 文件格式的本质是一种以文本存储的表格数据（使用 Excel 工具即可读写 csv 文件）。csv 文件的每行代表一行数据，每行数据中每个单元格内的数据以逗号隔开。

Python 提供了 csv 模块来读写 csv 文件。由于 csv 文件的格式本身比较简单（通常第一行是表头，用于说明每列数据的含义，接下来每行代表一行数据），因此使用 csv 模块读取 csv 文件也非常简单：
创建 csv 模块的读取器。
循环调用 csv 读取器的 next() 方法逐行读取 csv 文件内容即可。next() 方法返回一个 list 列表代表一行数据，list 列表的每个元素代表一个单元格数据。

本节使用的是 2017 年广州天气数据的 csv 文件（数据来源于 http://lishi.tianqi.com/ 网站。下面程序示范了使用 csv 读取器来读取 csv 文件的两行内容。

"""


import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = "guangzhou-2017.csv"


# 打开文件
with open(filename) as f:
    # 创建csv文件读取器
    reader = csv.reader(f)
    # 读取第一行.这行是表头数据
    header_row = next(reader)
    print(header_row)
    # 定义读取起始日期
    start_date = datetime(2017, 6, 30)
    # 定义结束日期
    end_date = datetime(2017, 8, 1)
    # 定义3个list列表作为展示的数据
    dates, highs, lows = [], [], []
    for row in reader:
        # 将第一列的值格式化为日期
        d = datetime.strptime(row[0], "%Y-%m-%d")
        # 只展示2017年7月的数据
        if start_date < d < end_date:
            dates.append(d)
            highs.append(int(row[1]))
            lows.append(int(row[2]))
# 配置图形
fig = plt.figure(dpi=128, figsize=(12, 9))

# 绘制最高气温的折线
plt.plot(dates, highs, c="red", label="最高气温",
         alpha=0.5, linewidth=3.0, linestyle="-.", marker="o")

# 再绘制一条折线
plt.plot(dates, lows, c="blue", label="最低气温",
         alpha=0.1, linewidth=3.0, linestyle="-.", marker="o"
         )

# 为两个数据的绘图区域填充颜色
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# 设置标题
plt.title("广州2017年7月最高气温和最低气温")

# 为两条坐标轴设置名称
plt.xlabel("日期")

# 该方法绘制斜着的日期标签
fig.autofmt_xdate()
plt.ylabel("气温(℃)")


# 显示图例
plt.legend()
ax = plt.gca()

# 设置右边坐标轴线的颜色(设置为none表示不显示)
ax.spines["right"].set_color("none")

# 设置顶部坐标轴线的颜色(设置为none表示不显示)
ax.spines["top"].set_color("none")
plt.show()
