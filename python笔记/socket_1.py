# coding:utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('jsonip.com', 80))

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buff = []
while True:
    d = s.recv(1024)
    if d:
        buff.append(d)
    else:
        break

s.close()

data = b''.join(buff)
print(data.decode('utf-8'))
# print(data.split(b'\r\n\r\n'))