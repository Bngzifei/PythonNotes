# -*- coding: utf-8 -*-
import socket
import time
from concurrent import futures


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


def process_way():
    """多进程方式"""
    workers = 10
    with futures.ProcessPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for _ in range(10)}
    return len([fut.result() for fut in futs])


t1 = time.time()
process_way()
t2 = time.time()
print(t2 - t1)
