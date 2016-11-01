# coding:utf-8

import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(5)

print('waiting for connection')

def tcplink(sock, addr):
    print('accept connection from', addr)
    print('thread process', threading.current_thread().name)



while True:
    sock, addr = server.accept()
    print('accept connection from ', addr)

    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

