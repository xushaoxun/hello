#!/usr/bin/python
# coding: utf-8

import requests
import sys
from selenium import webdriver
import time

reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://www.jd.com'

def requests_get():
    resp = requests.get(url)
    with open('jd1.html', 'w') as f:
        f.write(resp.text)

def scroll(n, i):
    return 'window.scrollTo(0, (document.body.scrollHeight/{0}) * {1});'.format(n, i)

def ff_get():
    firefox = webdriver.Firefox()
    firefox.maximize_window()
    firefox.get(url)

    n = 10
    for i in range(1, n+1):
        s = scroll(n, i)
        print s
        firefox.execute_script(s)
        time.sleep(1)

    print len(firefox.page_source)

    with open('jd2.html', 'w') as f:
        f.write(firefox.page_source)

    firefox.quit()

if __name__ == '__main__':
    #requests_get()
    ff_get()
