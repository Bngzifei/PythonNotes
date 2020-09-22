# -*- coding: utf-8 -*-
import socket
import time


def blocking_way():
    """同步阻塞"""
    sock = socket.socket()
    # blocking
    sock.connect(("example.com", 80))
    request = "GET / HTTP/1.0\r\nHost: example.com\r\n\r\n"
    sock.send(request.encode("ascii"))
    response = b""
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        # blocking  从socket中读取4K字节数据
        chunk = sock.recv(4096)
    return response


def sync_way():
    """同步方式"""
    res = []
    for i in range(10):
        res.append(blocking_way())
    print(len(res))
    return len(res)


t1 = time.time()
sync_way()
t2 = time.time()
print(t2 - t1)
