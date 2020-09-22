# -*- coding: utf-8 -*-
import socket
import time
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
stopped = False
urls_todo = {"/", "/1", "/2", "/3", "/4", "/5", "/6", "/7", "/8", "/9"}


class Future:

    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)


