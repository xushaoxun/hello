# coding:utf-8
import socket

HOST = '192.168.3.51'
PORT = 21567
ADDR = (HOST, PORT)
BUF = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while True:
    data = input('data to send:')
    if not data:
        break

    client.send(data.encode('utf-8'))
    print('data sent')
    data = client.recv(BUF)
    print('recv data: ', data)

client.close()