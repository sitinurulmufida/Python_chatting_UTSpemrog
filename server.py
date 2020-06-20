#program untuk server

import socket

listenerSocket = socket.socket()
serverIP ="0.0.0.0"
serverPort =2222
listenerSocket.bind((serverIP,serverPort))
listenerSocket.listen(0)
print("server siap menerima client")
while True:
	handlerSocket, addr = listenerSocket.accept()
	print ("sebuah client baru terkoneksi dengan alamat : ",addr)
	while True:
		message = input("masukkan pesan anda : ")
		handlerSocket.send(message)
		message = handlerSocket.recv(1024)
		print ("pesan dari client : ",message)
		pass
	pass