import sys
import time
from socket import *

serverPort = 1200 				#Port used by the client & server
serverSocket = socket(AF_INET, SOCK_DGRAM) 	#Initialize server socket
serverSocket.bind(('',serverPort))

while 1:
  print ("Server ready")
  message, clientAddress = serverSocket.recvfrom(2048) 	#Recieve the client's ping
  pingRecievedTime = time.time()			#Record the time at which the client's ping was recieved
  returnMessage = message + ","+ str(pingRecievedTime)  #Set up the return message
  serverSocket.sendto(returnMessage, clientAddress)     #Send the return message

