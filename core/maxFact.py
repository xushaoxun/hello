#!/usr/bin/python
# coding:utf-8


def max_factor(num):
    count = num/2
    while count > 1:
        if not (num % count):
            return count
        count -= 1
    else:
        return 1

for i in range(2, 100):
    print i, max_factor(i)
