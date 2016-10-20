#!/usr/bin/python
# coding:utf-8
import requests
import sys

def get_content(url):
    '''
    get content from an url
    '''
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception

    return r.text

class MyClass:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

if __name__ == '__main__':
    # utf-8 error
    reload(sys)
    sys.setdefaultencoding('utf-8')

    url = 'http://www.phei.com.cn'

    content = get_content(url)

    #print('50 chars: %s' % content[:50])
    print 'content length: %d kb' % (len(content) / 1024)
    if len(content) > 1024*40:
        print 'content > 4kb'
    else:
        print 'content < 4kb'

    #save1
    f = open('content.html', 'w')
    f.write(content)
    f.close()

    #save2
    with open('content2.html', 'w') as f:
        f.write(content)

    #read
    with open('content2.html', 'r') as f:
        print f.readlines()



    #class
    myc = MyClass('eagle')
    print myc.get_name()

