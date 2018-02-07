import socket
from time import time, sleep
def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print("connection from: " + str(addr))
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("from conneted user: " + str(data))
        pong = (str(data) + "," + str(time()))
        print("sending: " + str(data))
        c.send(pong)
    c.close
    

if __name__ == '__main__':
    Main()