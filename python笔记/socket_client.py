# coding:utf-8
import socket, random

ips = ['192.168.3.103', '127.0.0.1']
ip = random.choice(ips)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, 12345))

print('connet to server', ip)
while True:
    data = client.recv(1024)

    print('data recv: ', data.decode('utf-8'))
    data = input('input data:')
    if not data:
        break

    client.send(data.encode('utf-8'))

client.close()