# coding:utf-8
import time, threading

def loop():
    print('thread %s is running' % threading.current_thread().name)
    for i in range(5):
        print('thread %s >>> %d' % (threading.current_thread().name, i))
    print('thread %s end' % threading.current_thread().name)


print('thread %s is running' % threading.current_thread().name)
t = threading.Thread(target=loop, )
t.start()
t.join()
print('thread %s end' % threading.current_thread().name)

'''多线程和多进程最大的不同在于，
多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
而多线程中，所有变量都由所有线程共享，
所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
'''

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    print('thread: %s, balance=%d' % (threading.current_thread().name, balance))

def run_thread(n):
    for i in range(100):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, name='t1', args=(10,))
t2 = threading.Thread(target=run_thread, name='t2', args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()

'''
 ThreadLocal, 为每个thread保存各自变量
一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
'''

local = threading.local()
def process_student():
    std = local.student
    print('Hello, %s by %s' % (std, threading.current_thread().name))

def process_thread(student):
    local.student = student
    process_student()

t1 = threading.Thread(target=process_thread, args=('alice',), name='alice')
t2 = threading.Thread(target=process_thread, args=('bob',), name='bob')
t1.start()
t1.join()
t2.start()
t2.join()

#Thread & Process应该优先用process，更稳定
#Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
# 一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers
# 模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

import random, time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()