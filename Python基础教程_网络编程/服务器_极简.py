from asyncore import dispatcher
import socket
import asyncore


PORT = 5005


class ChatServer(dispatcher):

    def __init__(self, port):
        super(ChatServer, self).__init__()  # super的方式和下面的父类.初始化的方式本质是一样的
        # dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(("", port))
        self.listen(5)

    def handle_accept(self):
        conn, addr = self.accept()
        print("Connection attempt from", addr[0])


if __name__ == '__main__':
    s = ChatServer(PORT)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass
