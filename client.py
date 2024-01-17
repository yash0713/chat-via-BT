import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("c8:e2:65:cd:d7:fe",4))

try:
	while True:
		message = input("Client: ")
		client.send(message.encode("utf-8"))
		data = client.recv(1024)
		if not data:
			break
		print(f"Server: {data.decode('utf-8')}")
except OSError as e:
	pass

client.close()
