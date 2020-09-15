# -*- coding: utf-8 -*-
import threading
from threading import Event


def worker(event_obj, i):
    print('{i}号线程等待事件信号'.format(i=i))
    event_obj.wait()
    print('{i}号线程收到事件信号'.format(i=i))


event = Event()

for i in range(5):
    t = threading.Thread(target=worker, args=(event, i))
    t.start()

print('确认资源可用')
event.set()
