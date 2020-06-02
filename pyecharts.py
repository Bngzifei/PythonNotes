# coding:utf-8
from pyecharts.charts import Line
import pyecharts.options as opts
from pyecharts.globals import CurrentConfig

# 注意路径只到js/即可,自动设置文件名
CurrentConfig.ONLINE_HOST = "/static/js/"

# 绘制散点数据
xaxis_data = ['14:48:42', '14:48:43', '14:48:44', '14:48:45', '14:48:46',
              '14:48:47',
              '14:48:48', '14:48:49', '14:48:50', '14:48:51', '14:48:52',
              '14:48:53',
              '14:48:54', '14:48:55', '14:48:56']
yaxis_data = [0, 188, 850, 1522, 2159, 2806, 3455, 4149, 4800, 5470, 6099,
              6774, 7424,
              8077, 8744]
y2 = [14310, 16976, 19616, 22353, 24964, 27603]


def Line_charts(users, xaxis_data, yaxis_data, date) -> Line:
    """定义一个Line_charts函数"""
    c = Line()
    c.add_xaxis(xaxis_data=xaxis_data)

    # 设置图例信息
    c.add_yaxis(series_name=str(users) + "users" + "      " + "date:  " + date,
                y_axis=yaxis_data, is_smooth=True)
    # c.add_yaxis(series_name='400users', y_axis=y2)

    data_zoom = {
        "show": False,
        "title": {"zoom": "data zoom", "back": "data zoom restore"}
    }
    # 数据项设置,全局只设置一次
    c.set_global_opts(
        # 设置标题
        title_opts=opts.TitleOpts(title="不同users对应的TPM值"),
        # 设置图例is_show=False是 不显示图例
        legend_opts=opts.LegendOpts(is_show=True),
        # 设置提示项
        tooltip_opts=opts.TooltipOpts(trigger='axis',
                                      axis_pointer_type='cross'),
        # 工具箱的设置
        toolbox_opts=opts.ToolboxOpts(is_show=False,
                                      feature=opts.ToolBoxFeatureOpts(
                                          data_zoom=data_zoom))

    )

    return c

# 绘制图表
# c = Line_charts()
# c.render("second_line.html")
