#!/usr/bin/python
# coding:utf-8
import re

p = r'(\d{4})-(\d{2})-(\d{2})'
s1 = 'today is 2016-10-20'

m = re.search(p, s1)
if m:
    print m.start(), m.end(), m.group()


s2 = '2016-10-21 is tomorrow'
m = re.match(p, s2)
if m:
    print m.start(), m.end(), m.group(), m.groups()

url = 'http://www.baidu.com/news?from=2015-12-31&to=2016-10-31'
a = re.findall(p, url)
print a


print re.split(r'\s+', 'tomorrow    would   be  fine!')
