# coding:utf-8

import queue, time, sys
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_ip = '192.168.3.51'
print('connect to server')

manager = QueueManager(address=(server_ip, 5000), authkey=b'abc')
manager.connect()
task = manager.get_task_queue()
result = manager.get_task_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d*%d' % (n, n))
        r = n*n
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty')

print('worker done!')