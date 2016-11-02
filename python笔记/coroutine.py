# conding:utf-8

import asyncio, threading, time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

async def hello():
    print('hello world', threading.current_thread())

    # r = await asyncio.sleep(1)
    await time.sleep(1)

    print('hello world 2', threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# def wget(host):
#     print('wget ', host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     writer.close()
#
# loop1 = asyncio.get_event_loop()
# tasks1 = [wget(host) for host in ('www.sohu.com', 'www.baidu.com', 'www.163.com')]
# loop1.run_until_complete(asyncio.wait(tasks1))
# loop1.close()
