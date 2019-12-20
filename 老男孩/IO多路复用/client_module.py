import socket

sk = socket.socket()

sk.connect(('127.0.0.1',8090))

while True:
	inp=input('>>>')
	sk.send(inp.encode())
	data=sk.recv(1024)
	print(data.decode())