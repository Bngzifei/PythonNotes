import socket
import re

"""
PWS1.0: 在用户每次访问的时候都会返回一个固定数据比如Hello world
PWS2.0: 在用户每次访问的时候都会返回一个固定页面比如index.html
PWS3.0: 在用户每次访问的时候会根据用户资源请求返回对应的资源
1 接收请求报文
2 解析请求报文-得到用户的需求
3 根据用户的需求找到对应的资源
4 资源打包到HTTP响应报文
"""

def main():
    # 1 创建TCP的服务器套接字 设置套接字选项 绑定 监听
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(('', 8888))
    server_socket.listen(128)

    # 2 接受用户连接
    while True:
        client_socket, client_addr = server_socket.accept()
        print("接受到来自%s的连接请求" % str(client_addr))

        # 3 接收用户的请求报文
        request_data = client_socket.recv(4096)
        # print(request_data)
        request_str_data = request_data.decode()  # 解码

        # ps: 当用户 请求路径为/ 表示用户请求的是首页homepage
        # 4 解析用户请求 获取到用户的资源请求路径
        result = re.search(r"^\w+ (/\S*)", request_str_data)

        # 4.1 判断 是否 提取成功 成功就可以取出值; 不成功不能取出 结束
        if not result:
            print("HTTP请求报文格式错误")
            client_socket.close()
            continue

        # GET /index.html  如果执行到这里一定是匹配成功的  因为失败的已经continue了
        # 4.2 获取用户的请求路径 信息  资源路径 + /index.html
        path_info = result.group(1)

        # 4.3 潜规则 web服务器都会在用户请求/ 自动返回/index.html
        if path_info == '/':
            path_info = "/index.html"

        # 5 返回固定文件的数据作为响应体 打包到响应报文 中  static + /index.html
        with open("static" + path_info, "rb") as file:
        # with open("index.html", "rb") as file:
            # html_data是二进制数据
            html_data = file.read()
        #                响应行             响应头{0,}            空行               响应体数据
        response_data = ("HTTP/1.1 200 OK\r\nServer: PWS3.0\r\n"+"\r\n").encode() + html_data
        client_socket.send(response_data)

        # 一次请求响应就关闭 - 短连接
        client_socket.close()



if __name__ == '__main__':
    main()

