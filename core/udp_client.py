# coding:utf-8

import socket

HOST = '192.168.3.51'
PORT = 21567
ADDR = (HOST, PORT)
BUFSIZE = 1024

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input('data to send:')
    if not data:
        break
    clientSock.sendto(data.encode('utf-8'), ADDR)
    data, addr = clientSock.recvfrom(BUFSIZE)
    if not data:
        break

    print('data recieve', data.decode('utf-8'))

clientSock.close()
