# -*- coding: utf-8 -*-
import threading
import time


class htmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        # 内部维护的计数器加1，并通知内部维护的condition通知acquire
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            # 内部维护的计数器减1，到0就会阻塞
            self.sem.acquire()
            html_thread = htmlSpider("http://baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == "__main__":
    # 如果直接开20个htmlSpider线程，20个线程是同时执行的，
    # 现在要限制同时执行能执行三个，就可以使用信号量来控制：
    # 设置同时最多3个
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()
