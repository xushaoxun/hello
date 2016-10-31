#!/usr/bin/python
# coding:utf-8

with open('idcheck.py') as f:
    print sum([len(word) for line in f for word in line.split()])
