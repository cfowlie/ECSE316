import sys
import time
from socket import *

serverPort = 1200 
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))

while 1:

  message, clientAddress = serverSocket.recvfrom(2048)
  pingRecievedTime = time.time()
  returnMessage = message + ","+ str(pingRecievedTime)
  serverSocket.sendto(returnMessage, clientAddress)

