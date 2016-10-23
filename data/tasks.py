#!/usr/bin/python
# coding:utf-8

from celery import Celery, platforms
import requests
from bs4 import BeautifulSoup

# 生成celery实例。第一个参数为本模块名，第二个参数为broker url
# 表示Celery将连接各云端本地的redis。0表示redis默认数据库0
app = Celery('tasks', broker = 'redis://localhost:6379/0')

#结果存放位置。如果需要取回执行结果就需要这句
app.conf.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

#如果以root身份运行需要这句
platforms.C_FORCE_ROOT = True

@app.task
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


