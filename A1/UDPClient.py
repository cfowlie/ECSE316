import time
import sys
from socket import *


serverName = '142.157.20.166' //Server's IP Address
serverPort = 1200             //Port used by server & client
clientSocket = socket(AF_INET, SOCK_DGRAM)  //Initialize the client socket
clientSocket.settimeout(1)    //Make the client wait no more than one second
			      //before considering the message lost
for i in range (10):          //Send 10 pings
  pingSentTime = time.time()  //Record the time the ping was sent
  messageID = "Ping ID: " + str(1000 + i) //Ping's ID
  clientSocket.sendto(messageID,(serverName, serverPort))  //Send the message 
  							   to the server
  try:

    returnMessage, serverAddress = clientSocket.recvfrom(2048) //Read server response & store it
    pongRecievedTime = time.time()       		       //Record the time the server response was recieved
    roundTripTime = pongRecievedTime-pingSentTime              //Calculate round trip time
    pingRecievedTime = returnMessage.split(',')                //Split the return message to recover the timestamp sent by the server
    print ("--------------------------------------------")
    print ("")
    print ("Ping ID: ", messageID)
    print ("Ping successfully sent at: ", pingSentTime)
    print ("Ping successfully recieved by server at : ",pingRecievedTime[1]) 
    print ("Pong successfully recieved at: ", pongRecievedTime)
    print ("Round trip time is: ", roundTripTime)
    print ("")

  except timeout:			//If the server response was larger than 1 second, assume the message was lost.

    print "Message Lost."
