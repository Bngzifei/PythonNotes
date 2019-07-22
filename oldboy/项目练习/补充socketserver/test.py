import socketserver


class MySocket(socketserver.BaseRequestHandler):
	def handle(self):
		pass


s = socketserver.ThreadingTCPServer((), MySocket)
s.serve_forever()
