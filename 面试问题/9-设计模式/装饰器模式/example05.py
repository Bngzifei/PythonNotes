# -*- coding: utf-8 -*-
import time
import six
from oslo_log import log
import requests

LOG = log.getLogger(__name__)


def retry(retry_times=3, interval=5, ignore=False):
    def _wrapper(func):
        @six.wraps(func)
        def __wrapper(*args, **kwargs):
            # 初始化一个实例对象
            Retry_obj = Retry(func, retry_times, interval, ignore)
            # 实例对象(): 调用实例,就是 执行 __call__() 方法
            return Retry_obj(*args, **kwargs)

        return __wrapper

    return _wrapper


class Retry(object):
    """任务重试器"""

    def __init__(self, func, retry_times=3, interval=5, ignore=False):
        self.func = func
        # retry_times等于-1表示重试无限次
        self.retry_times = retry_times
        self.attempt_times = 0
        self.interval = interval
        # 超出重试次数仍然失败后，是否忽略异常
        self.ignore = ignore

    def __call__(self, *args, **kwargs):
        while True:
            try:
                result = self.func(*args, **kwargs)
            except Exception as ex:
                # 计数器:统计重试的次数
                self.attempt_times += 1
                LOG.error(f'{self.attempt_times} time call func: {self.func.__name__} fail, exception: {ex}')
                # 能执行到这里,就已经说明重试过程已经完成
                if self.retry_times != -1 and self.attempt_times >= self.retry_times:
                    # 忽略异常情况下直接break,退出循环
                    if self.ignore:
                        break
                    # raise: 写了就把当前捕获的异常直接抛出,同时阻塞了程序继续运行
                    raise
                else:
                    time.sleep(self.interval)
            else:
                return result


@retry(retry_times=3, interval=2, ignore=True)
def request_github(url):
    """请求github"""
    with requests.Session() as session:
        ret = session.get(url)
        print(ret)


if __name__ == '__main__':
    github_url = "https://www.google.com/"
    request_github(github_url)
