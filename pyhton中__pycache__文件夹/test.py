# coding:utf-8


def hahha():
    print("哈哈哈")


# hahha()

# print(__name__)  # 本文件中没有涉及到import 导入 操作,所以这里的__name__就是 __main__,

# 如果这里的test.py文件被其他的.py文件导入,那么在其他文件中,这里的__name__就是 test.py的
# 文件的名字.即:__name__== 文件名 test

if __name__ == '__main__':
    """可执行的代码:就是调用的部分,不是定义的部分"""
    hahha()
    print(__name__)
