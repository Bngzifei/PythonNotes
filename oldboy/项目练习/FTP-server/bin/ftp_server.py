import sys,os
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)  # 自己添加环境变量

from core import main

"""启动文件,程序入口"""
if __name__ == '__main__':
    main.ArgvHandler()
