#!/usr/local/bin/python
# coding:utf-8
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

urls_dict = {
        '电子工业出版社': 'http://www.phei.com.cn',
        '在线资源': 'http://www.phei.com.cn',
        'xyz': 'www.phei.com.cn',
        }

s = set()
for k, v in urls_dict.items():
    if v in s:
        print '%s 已经取过' % v
    else:
        try:
            r = requests.get(v)
        except Exception as e:
            print '%s错误: %s' % (v, e)
            continue
        content = r.text
        with open('%s.txt' % k, 'w') as f:
            f.write(content)
        print '%s 读取成功.大小%dkb' % (v, len(content) / 1024)
        s.add(v)


