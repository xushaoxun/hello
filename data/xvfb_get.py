#!/usr/bin/python
# coding:utf-8

from selenium import webdriver
import time

url = 'http://www.phei.com.cn'
ff = webdriver.Firefox()
ff.get(url)
print len(ff.page_source)
print ff.page_source
time.sleep(5)
ff.close()

