# -*- coding: utf-8 -*-
import threading
from threading import Event


def print_a(e1, e2):
    for item in [1, 3, 5]:
        e1.wait()
        print(item)
        e1.clear()
        e2.set()


def print_b(e1, e2):
    for item in [2, 4, 6]:
        e1.wait()
        print(item)
        e1.clear()
        e2.set()


e1, e2 = Event(), Event()
t1 = threading.Thread(target=print_a, args=(e1, e2))
t2 = threading.Thread(target=print_b, args=(e2, e1))
t1.start()
t2.start()
e1.set()
