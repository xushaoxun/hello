# coding:utf-8

import socket

HOST = '192.168.3.51'
PORT = 21567
ADDR = (HOST, PORT)
BUFSIZE = 1024

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(ADDR)

while True:
    data = input('data to send:')
    if not data:
        break
    clientSock.send(data.encode('utf-8'))
    data = clientSock.recv(BUFSIZE)
    print('data recieve', data.decode('utf-8'))

clientSock.close()
