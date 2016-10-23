#!/usr/bin/python
# coding:utf-8

import time
from celery import Celery
from threading import Thread

redis_ips = ['redis://192.168.3.123:6379/0', 'redis://192.168.3.22:6379/0']

def send_task_and_get_result(idx, from_page, to_page):
    redis_server = redis_ips[idx]
    print 'redis:', redis_server

    app = Celery('tasks', broker = redis_server)
    app.conf.CELERY_RESULT_BACKEND = redis_server
    result = app.send_task('tasks.get_urls_in_pages',  args = (from_page, to_page))

    print redis_server, result.get()

if __name__ == '__main__':
    page_ranges = [(1,30), (31, 60)]

    t1 = time.time()

    th_list = []
    for idx, pages in enumerate(page_ranges):
        th = Thread(task = send_task_and_get_result, args = (idx, pages[0], pages[1]))
        th_list.append(th)
    for th in th_list:
        th.start()
    for th in th_list:
        th.join()

    t2 = time.time()
    print '使用时间:', (t2-t1)


