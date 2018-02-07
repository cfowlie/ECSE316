import time
import sys

from socket import *
serverPort = 1200
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
	connectionSocket, addr = serverSocket.accept()
	message = connectionSocket.recv(2048)
	pingRecievedTime = time.time()
	returnMessage = (message, pingRecievedTime)
	connectionSocket.send(returnMessage)
	connectionSocket.close()
