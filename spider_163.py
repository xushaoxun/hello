#!/usr/bin/python
#coding:utf-8

import urllib2
import bs4

url = 'http://www.163.com'

content = urllib2.urlopen(url).read().decode('gbk').encode('utf-8')

soup = bs4.BeautifulSoup(content)

links = bs4.select('li a[href]')

result = []
for link in links:
    href = link.attrs['href']
    title = link.text
    if '.html' in href and '163.com' in href and len(title) > 4:
        result.append(link)


