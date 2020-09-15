# -*- coding: utf-8 -*-

"""
例子:有一个全局的计数num，每个线程获取这个全局的计数，根据num进行一些处理，然后将num加1.

但是运行结果是不正确的：
问题产生的原因就是没有控制多个线程对同一资源的访问，对数据造成破坏，使得线程运行的结果不可预期。这种现象称为“线程不安全”。
"""
import threading
import time

num = 0


class MyThread(threading.Thread):

    def run(self):
        global num
        time.sleep(1)
        num = num + 1
        msg = self.name + ' set num to ' + str(num)
        print(msg)


def test():
    for i in range(10000):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    test()
