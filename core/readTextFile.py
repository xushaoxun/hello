#!/usr/bin/python
# coding:utf-8

fname = raw_input('file to read:')

try:
    with open(fname) as f:
        for line in f:
            print line
except IOError as e:
    print e
