"""
注意:windows系统是没有fork模式的

"""

from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler


class Server(ForkingMixIn, TCPServer):
    pass


class Handler(StreamRequestHandler):

    def handler(self):
        addr = self.request.getpeername()
        print("Got connnection from :", addr)
        self.wfile.write("Thank you for connecting")


server = Server(("", 1234), Handler)
server.serve_forever()



