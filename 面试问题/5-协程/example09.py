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


class Crawler:

    def __init__(self, url):
        self.url = url
        self.response = b""

    def fetch(self):
        sock = socket.socket()
        sock.setblocking(False)

        try:
            sock.connect(("example.com", 80))
        except BlockingIOError:
            pass

        f = Future()

        def on_connected():
            f.set_result(None)

        selector.register(sock.fileno(), EVENT_WRITE, on_connected)
        yield f
        selector.unregister(sock.fileno())
        request = "GET {0} HTTP/1.0\r\nHost: example.com\r\n\r\n".format(self.url)
        sock.send(request.encode("ascii"))

        global stopped
        while True:
            f = Future()

            def on_readable():
                f.set_result(sock.recv(4096))

            selector.register(sock.fileno(), EVENT_READ, on_readable)
            chunk = yield f
            selector.unregister(sock.fileno())
            if chunk:
                self.response += chunk
            else:
                urls_todo.remove(self.url)
                if not urls_todo:
                    stopped = True
                break
