import os
import psutil


def show_memory_info(hint):
    """显示当前 python 程序占有的内存大小"""
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024 / 1024
    print("{} memory used: {} MB".format(hint, memory))


def func():
    show_memory_info("initial")
    a = [i for i in range(1000000000000)]
    show_memory_info("after a created")


func()
show_memory_info("finished")
