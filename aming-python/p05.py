#!/usr/bin/python
# coding:utf-8

i = raw_input('Input number:')
if(i.isdigit() ):
    i = int(i)
    dl = range(1, i/2+1)
    print [d for d in dl if i%d==0]

