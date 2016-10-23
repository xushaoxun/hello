#!/usr/bin/python
# coding:utf-8

import time

def log(func):
    def wrapper(*args, **kwargs):
        print 'call %s()' % func.__name__
        return func(*args, **kwargs)
    return wrapper

#相当于now = log(now)
@log
def now():
    print '2015-10-23'

now()
