# coding:utf-8

import socket, threading, time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(5)

print('waiting for connection')

def tcplink(sock, addr):
    print('accept connection from', addr)
    print('thread process', threading.current_thread().name)
    sock.send(b'Hello')

    while True:
        data = sock.recv(1024)
        if not data:
            break
        sock.send((b'[%s] %s' % (time.ctime(), data.decode('utf-8'))).encode('utf-8'))
    sock.close()
    print('connection closed')


while True:
    sock, addr = server.accept()
    print('accept connection from ', addr)

    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

