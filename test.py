#!/usr/bin/python
# coding:utf-8

'''doc'''

import types

for x in xrange(1, 10):
    print x,


class ClassName(object):
    """docstring for ClassName"""

    def __init__(self):
        super(ClassName, self).__init__()

a = 1
b = 1
print id(a), id(b)
print a is b

print(__doc__)

print 'hello'

c = ClassName()
print isinstance(1, int)
print isinstance(c, ClassName)
