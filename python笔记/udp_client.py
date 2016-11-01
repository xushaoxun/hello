# coding:utf-8
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'1234', b'abc', b'']:
    print('sent data', data)
    client.sendto(data, ('192.168.3.51', 12345))

    data, addr = client.recvfrom(1024)
    print('data recv:', data.decode('utf-8'))

client.close()