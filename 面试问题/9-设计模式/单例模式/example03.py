# -*- coding: utf-8 -*-
from functools import wraps
from threading import Lock


def singleton(cls):
    """线程安全的单例装饰器"""
    instances = {}
    locker = Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President():
    """总统(单例类)"""
    pass


@singleton
class Life():
    """生命(单例类)"""
    pass


pre1 = President()
pre2 = President()
life1 = Life()
life2 = Life()

print(bool(id(pre1) == id(pre2)))
print(bool(id(life1) == id(life2)))
