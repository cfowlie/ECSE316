import time
import sys
from socket import *


serverName = '142.157.20.166'
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range (10):
  pingSentTime = time.time()
  messageID = "Ping ID: " + str(1000 + i)
  clientSocket.sendto(messageID,(serverName, serverPort))
  
  try:

    returnMessage, serverAddress = clientSocket.recvfrom(2048)
    pongRecievedTime = time.time()
    roundTripTime = pongRecievedTime-pingSentTime
    pingRecievedTime = returnMessage.split(',')
    print ("--------------------------------------------")
    print ("")
    print ("Ping ID: ", messageID)
    print ("Ping successfully sent at: ", pingSentTime)
    print ("Ping successfully recieved by server at : ",pingRecievedTime[1]) 
    print ("Pong successfully recieved at: ", pongRecievedTime)
    print ("Round trip time is: ", roundTripTime)
    print ("")

  except timeout:

    print "Message Lost."
