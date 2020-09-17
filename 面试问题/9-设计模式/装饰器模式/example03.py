# -*- coding: utf-8 -*-
"""
<i> 斜体
<b> 加粗,黑体

多个装饰器:同时扩展多个功能
"""


def makeBold(func):
    """加粗"""

    def inner(*args, **kwargs):
        return '<b>' + func() + '</b>'

    return inner


def makeItalic(func):
    """倾斜"""

    def inner(*args, **kwargs):
        return '<i>' + func() + '</i>'

    return inner


@makeItalic
@makeBold
@makeItalic
def f1():
    return '人生苦短,我用Python'


print(f1())
# 执行结果: <i><b><i>人生苦短,我用Python</i></b></i>

# 执行顺序,先倾斜,后加粗, 类似于穿衣服,内衣先,外套后

# 灵魂代码理解:  f1 = makeItalic(f1)

# 1.>f11 = makeItalic(f1) f11是  makeItalic 里面的inner ;
# 2.>f111 = makeBold(f11) f111是makeBold 里面的inner

# 一步理解:  f1 = makeBold(makeItalic(f1))    ------> 简单理解就是多层装饰了
# 类似于寄快递,自己包一层之后快递小哥也会帮你再 包一层.

# 执行顺序一定是先去执行最内层的.<最内层的装饰器先完成装饰>
# 但是: 是最外层的最先开始装饰,它需要内层的装饰完成才能去装饰.
