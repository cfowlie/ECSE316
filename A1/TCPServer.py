import time
import sys

from socket import *
serverPort = 1200 #Port used by the client & server
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
	connectionSocket, addr = serverSocket.accept()
	message = connectionSocket.recv(2048) 					#Recieve the client's ping
	pingRecievedTime = time.time()							#Record the time at which the client's ping was recieved
	returnMessage =  message + ","+ str(pingRecievedTime)	#Prep return msg
	connectionSocket.send(returnMessage)					#Send response
