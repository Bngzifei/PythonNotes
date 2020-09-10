# -*- coding: utf-8 -*-
import grpc
from example import data_pb2, data_pb2_grpc

# 如果不是在同一台机器上面进行演示,记得 这里的ip 写 server服务所在的真正ip,
_HOST = 'localhost'
_PORT = '8080'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = data_pb2_grpc.FormatDataStub(channel=conn)
    response = client.DoFormat(data_pb2.Data(text='hello,world!'))
    print("received: " + response.text)


if __name__ == '__main__':
    run()
