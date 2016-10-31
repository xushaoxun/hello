# coding:utf-8
from multiprocessing import Process, Pool
import os, time, random

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

def long_time_task(name):
    print('run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    stop = time.time()

    print('task use %.2f seconds' % (stop - start))

if __name__ == '__main__':

    print('Parent process id=%s' % os.getpid())
    proc = Process(target=run_proc, args=('child',))
    proc.start()
    proc.join()

    #use pool
    pool = Pool(4)
    for i in range(5):
        pool.apply_async(long_time_task, args=(i,))
    pool.close()
    pool.join()
    print('end all process')

