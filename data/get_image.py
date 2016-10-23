#!/usr/bin/python
# coding:utf-8

import requests
import urlparse
import os

from bs4 import BeautifulSoup

def get_imgs(url):
    #prepare dir

    if not os.path.exists('res'):
        os.mkdir('res')
    os.chdir('res')

    host = 'http://' + urlparse.urlparse(url).netloc

    '''get images from page'''
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception

    bs = BeautifulSoup(resp.text, 'lxml')
    imgs = bs.find_all('img')
    for img in imgs:
        src = img['src']
        if src.startswith('/'):
            src = host + src

        file_name = src.split('/').pop()

        #get images and save
        resp = requests.get(src)
        with open(file_name, 'wb') as f:
            f.write(resp.content)
        print 'save file: ', src

if __name__ == '__main__':
    url = 'http://www.phei.com.cn/'
    get_imgs(url)
