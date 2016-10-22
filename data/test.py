#!/usr/bin/python
# coding:utf-8

import requests

'''
url = 'http://www.phei.com.cn/module/goods/wssd_content.jsp?bookid=47780'
resp = requests.get(url)
#print resp.text
print resp.encoding
print resp.status_code
print resp.url

resp.close()

url = 'http://jsonip.com'
resp = requests.get(url)
j = resp.json()
print type(j)
resp.close()
'''

url = 'http://192.168.0.123:9999/get'
params = {'name': 'eagle', 'age': 36}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.01'}
resp = requests.get(url, params, headers=headers)
resp = requests.get(url, params)
print resp.content
#print resp.json()

'''
#post
url = 'http://192.168.0.123:9999/post'
data = {'name': 'eagle', 'age': 36}
resp = requests.post(url, data)
print resp.json()
'''
