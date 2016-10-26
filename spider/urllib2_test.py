#!/usr/bin/python
# coding: utf-8

import urllib
import urllib2
import random

'''
为何要限制爬虫？防止竞争对手抓取
robots.txt
User-agent: Baiduspider
Disallow: /
禁止百度蜘蛛
'''
url = 'http://blog.csdn.net/yuanmeng001'
html = urllib.urlopen(url)
print html.read()	#403 Forbidden
print html.getcode()	#403


'''
怎么模仿浏览器访问？
Header: 
Referer
User-Agent
'''
user_agents = ['Mozilla firefox', 'Chrome']

headers = {
	'GET': url, 
	'User-Agent': random.choice(user_agents),
	'Host': 'blog.csdn.net',
	'Referer': 'http://blog.csdn.net/'

	}
req = urllib2.Request(url, headers=headers)
# req.add_header('GET', url)
# req.add_header('User-Agent', 'Mozilla/5.0')
# req.add_header('Host', 'blog.csdn.net')
# req.add_header('Referer', 'http://blog.csdn.net')

html = urllib2.urlopen(req)

print html.read()

#代理ip，假的用户信息结合起来基本上可以让服务器无法认出是不是爬虫