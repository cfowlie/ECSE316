import socket
from time import time, sleep

def Main():
    host = '142.157.20.166'
    port = 1200

    s = socket.socket()
    s.connect((host,port))

    #change while loop to for loop
    #can use index of for loop as unique ID's
    results = {}
    for i in range(0, 10):
        s.send(str(i))
        startTime = time()
        data = s.recv(1024)
        # while True:
        #     data = s.recv(1024)
        #     if data:
        #         break
        #     #do nothing else
        intmd = str(data).split(',')
        id = intmd[0]
        endTime= intmd[1]
        results[str(id)] = endTime
        print("Received from server: " + str(float(endTime) - startTime))
    s.close()
if __name__ == '__main__':
    Main()
    # #If want to use more authentic unique ID's import uuid and call uuid4()
    # while message != 'q':
    #     s.send(message)
    #     data = s.recv(1024)
    #     print("Received from server: " + str(data))
