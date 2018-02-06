import time
import sys
from socket import *


serverName = 
serverPort = 1
clientSocker = socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range (5):
  pingSentTime = time.time()
  messageID = 1000 + i
  clientSocket.sendto(message,(serverName, serverPort))
  
  try:

    returnMessage, serverAddress = clientSocket.recvfrom(2048)
    pongRecievedTime = time.time()
    roundTripTime = pongRecievedTime-pingSentTime
    print ("Ping ID: %d", messageID)
    print ("Ping successfully sent at: %d", pingSentTime)
    print ("Ping successfully recieved by server at :%d",returnMessage(1)) 
    print ("Pong successfully recieved at: %d", pongRecievedTime)
    print ("Round trip time is: %d", roundTripTime)
    
  except timeout:

    print "Message Lost."
