import socket

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("www.pythonlearn.com", 80))
mysock.send("GET http://wwww.pythonlearn.com/code/intro-short.txt")

while true:
	data=sock.recv(512)
	if (len(data)<1)
		break
	print data

mysock.close()