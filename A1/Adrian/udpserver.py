import socket
from time import time, sleep
def Main():
    host = '127.0.0.1'  #for ass, we will be connecting to another server, so this cariable and file are unnecessary
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server started")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message from: " + str(addr))
        print("From connect user: ")
        recvTime = str(time())
        data = data + ',' + recvTime
        s.sendto(data.encode('utf-8'), addr)
    s.close

if __name__ == '__main__':
    Main()