#!/usr/local/bin/python
# coding:utf-8

import re

def isnum(s):
    p = '^\d*\.?\d*$'
    m = re.match(p, s)
    if m:
        return True
    return False

def issu(d):
    if d==1 or d==2:
        return True
    n = d/2
    l = [i for i in xrange(2,n+1) if d%i ==0]

    if l:
        return False
    else:
        return True

for i in range(1, 10):
    print '%d is su? %s' % (i, issu(i))

########################
from collections import Counter
def cn(s):
    return Counter([c for c in s if c.isalpha()])

s='''aba *&& 23423 sdf :wsde helsdf'''
c = cn(s)
print c

print sorted(c.items(), reverse = True)

if __name__ == '__main__':
    print '__main__'