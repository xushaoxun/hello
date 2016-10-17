#!/usr/bin/python
#coding:utf-8

import re
import os

depts = ['aa', 'bb']
for d in depts:
    try:
        os.mkdir(d)
    except OSError as e:
        print '目录【%s】创建失败。原因%s' % (d, e.strerror)

print '你好'
