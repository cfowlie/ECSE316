import sys
import time
from socket import *

serverPort = 
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))

while 1:

  message, clientAddress = serverSocket.recvfrom(2048)
  pingRecievedTime = time.time()
  returnMessage = (message, pingRecievedTime)
  serverSocket.sendTo(returnMessage, clientAddress)

