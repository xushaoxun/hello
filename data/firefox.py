#!/usr/bin/python
# coding:utf-8

from selenium import webdriver
import time
import sys
import matplotlib.pyplot as plt

reload(sys)
sys.setdefaultencoding('utf-8')

def performance(n, css_val, image_val, js_flag):
    loading_time = []

    for i in range(0, n):
        #preference
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference('permissions.default.stylesheet',css_val)
        firefox_profile.set_preference('permissions.default.image', image_val)
        firefox_profile.set_preference('javascript.enabled', js_flag)
        firefox_profile.update_preferences()

        url = 'http://www.phei.com.cn'
        firefox = webdriver.Firefox(firefox_profile)
        print 'start..'
        t1 = time.time()
        firefox.get(url)
        t2 = time.time()
        t = t2 - t1
        print 'loading time:', t
        loading_time.append(t)
        print '*'*20


        #time.sleep(5)
        firefox.quit()
    return [x for x in range(1, n+1)], loading_time

if __name__ == '__main__':
    '''
    x1_list, y1_list = performance(1, 2, 2, False)
    x2_list, y2_list = performance(1, 1, 1, True)

    ava_y1 = sum(y1_list) / len(y1_list)
    ava_y2 = sum(y2_list) / len(y2_list)

'''
    x1_list =[1,2]
    y1_list =[4,5]
    x2_list =[1,2]
    y2_list =[6,10]
    plt.title('Compare loading time')
    plt.xlabel('Test number')
    plt.ylabel('Loading time')
    plt.plot(x1_list, y1_list, 'go:', label='x1')
    plt.plot(x2_list, y2_list, 'go:', label='x2')
    plt.legend()
    print 1
    plt.show()


