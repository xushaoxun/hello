#!/usr/bin/python
# coding:utf-8

import time
import requests
from bs4 import BeautifulSoup
import threading
import multiprocessing
import sys
import gevent
from gevent import monkey

reload(sys)
sys.setdefaultencoding('utf-8')

page_ranges = [(i*10-9, i*10) for i in range(1, 6)]

# 抓取http://www.phei.com.cn/module/goods/searchkey.jsp?Page=x&goodtypeid=1&goodtypename=%E8%AE%A1%E7%AE%97%E6%9C%BA
def get_urls_in_pages(from_page, to_page):
    url_tpl = 'http://www.phei.com.cn/module/goods/searchkey.jsp?Page={}&goodtypeid=1&goodtypename=%E8%AE%A1%E7%AE%97%E6%9C%BA'
    print 'get urls from %d to %d' % (from_page, to_page)

    url_list= [url_tpl.format(i) for i in range(from_page, to_page+1)]

    url_book_d = {}

    for url in url_list:
        resp = requests.get(url)
        text = resp.text
        if 'Apache Tomcat/6.0.13 - Error report' in text:
            continue

        bs = BeautifulSoup(text, 'lxml')
        a_list = bs.find_all('a', target='_blank')

        for a in a_list:
            book_name = a.text.strip()
            href = a['href']
            if book_name and 'bookid' in href:
                url_book_d['http://www.phei.com.cn'+href] = book_name

    return url_book_d

def non_thread():
    print 'non thread process'
    t1 = time.time()

    for f,t in page_ranges:
        r = get_urls_in_pages(f, t)

    t2 = time.time()

    print 'using %d seconds' % (t2-t1)

#使用线程
def use_thread():
    print 'use thread'
    page_ranges = [(i*10-9, i*10) for i in range(1, 6)]
    t1 = time.time()

    thread_list = []
    for f,t in page_ranges:
        t = threading.Thread(target=get_urls_in_pages, args=(f,t))
        thread_list.append(t)

    #for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    t2 = time.time()
    print 'using %d seconds' % (t2 - t1)

def use_multi_processing():
    print 'use multi processing'
    global page_ranges

    t1 = time.time()

    thread_list = []
    for f,t in page_ranges:
        pool = multiprocessing.Pool(processes = 4)  #4个进程的进程池
        pool.apply_async(get_urls_in_pages, (f, t))
    pool.close()
    pool.join()

    t2 = time.time()
    print 'using %d seconds' % (t2 - t1)

def use_gevent():
    print 'use gevent'
    t1 = time.time()

    monkey.patch_all()

    jobs = []
    for f,t in page_ranges:
        jobs.append(gevent.spawn(get_urls_in_pages, f, t))
    gevent.joinall(jobs)

    t2 = time.time()
    print 'use %d seconds' % (t2 - t1)


if __name__ == '__main__':
    #non_thread()

    #use_thread()

    #use_multi_processing()

    use_gevent()
