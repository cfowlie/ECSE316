import socket
from time import time, sleep

def Main():
    host = '127.0.0.1'
    port = 5001

    server = ('127.0.0.1', 5000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    #change while loop to for loop
    #can use index of for loop as unique ID's
    timeout = 1000
    results = {}
    for i in range(0, 10):
        s.sendto(str(i).encode('utf-8'), server)
        startTime = time()
        while (time() - startTime < timeout):
            data, addr = s.recvfrom(1024)
            if data:
                break
            #do nothing else
        if data:
            intmd = str(data).split(',')
            id = intmd[0]
            endTime= intmd[1]
            print("reached here")
            results[str(id)] = endTime
            print("Received from server: " + str(float(endTime) - startTime))
        else:
            results[str(i)] = "dropped"
    s.close

if __name__ == '__main__':
    Main()
    #If want to use more authentic unique ID's import uuid and call uuid4()
    # while message != 'q':
    #     s.send(message)
    #     data = s.recv(1024)
    #     print("Received from server: " + str(data))