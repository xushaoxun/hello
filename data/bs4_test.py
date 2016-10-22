#!/usr/bin/python
# coding:utf-8

from bs4 import BeautifulSoup
import requests

url = 'http://www.phei.com.cn/module/goods/wssd_content.jsp?bookid=47777'
f =  requests.get(url)
bs = BeautifulSoup(f.text, 'lxml')

print bs.a.text


f.close()
