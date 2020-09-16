# -*- coding: utf-8 -*-
import threading
import time

num = 0
# 互斥锁
mutex = threading.Lock()


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(bool(1)):
            num = num + 1
            msg = self.name + ' set num to ' + str(num)
            print(msg)
            mutex.release()


def test():
    for i in range(10000):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    test()
