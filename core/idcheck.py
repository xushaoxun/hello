#!/usr/bin/python
# coding:utf-8

import string

alphas = string.ascii_letters + '_'
nums = string.digits

print 'idchecker 1.0'
print 'at least 2 chars'

s = raw_input('input: ')
if len(s) > 1:
    if s[0] in alphas:
        for i in s:
            if i in nums + alphas:
                pass
            else:
                print '%s not valid' % i
                break
        else:
            print 'pass'
    else:
        print 'first letter invalid'
else:
    print 'at least 2 chars'
