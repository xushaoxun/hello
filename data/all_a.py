#!/usr/bin/python
# coding:utf-8
import requests
import bs4
import re

url = 'http://www.phei.com.cn/module/goods/searchkey.jsp?goodtypeid=1&goodtypename=%E8%AE%A1%E7%AE%97%E6%9C%BA'

f = requests.get(url)

code = f.status_code
if code != 200:
    raise Exception('status error, code %d' % code)

content = f.text

bs = bs4.BeautifulSoup(content, 'html.parser')
a_list = bs.find_all('a')

for l in a_list:
    if l.text and '/module/goods/wssd_content.jsp' in l['href']:
        print l.text.strip(), l['href']
print '-'*80
div_list = bs.find_all('div', attrs={'style':re.compile(r'width:730px.*')})
for d in div_list:
    for l in d.find_all('a'):
        if l.text.strip():
            print l.text.strip(), l['href']

