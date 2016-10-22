#!/usr/bin/python
# coding:utf-8

from bs4 import BeautifulSoup
import sys
import requests
import xlwt

reload(sys)
sys.setdefaultencoding('utf-8')

#10 pages
urls = ['http://www.phei.com.cn/module/goods/searchkey.jsp?Page={}&goodtypeid=1&goodtypename=%E8%AE%A1%E7%AE%97%E6%9C%BA'.format(x) for x in range(1, 3)]

page_info_keys = ('URL', u'书名', u'作译者', u'出版时间', u'千字数', u'版次', u'页数', u'开本', u'内容简介')

# 取得页面数据
def get_page_data(url):
    f = requests.get(url)
    # page error
    if 'Apache Tomcat/6.0.13 - Error report' in f.text:
        return None

    bs = BeautifulSoup(f.text, 'lxml')
    tds = bs.find_all('td', height=20)

    page_info = {}
    for td in tds:
        if '：' in td.text:
            key = td.text.strip().split('：')[0].replace(u'\xa0', '')   #替换全角空格
            value = td.text.strip().split('：')[1]
            if key in page_info_keys:
                page_info[key] = value

    # 内容简介
    instr_td = bs.find('td', class_='line_h24 f12_grey pad_t20 pad_bot20')
    page_info[u'内容简介'] = instr_td.text

    print '获取内容%s' % url

    return page_info

# end get_page


page_info_list = []

for url in urls:
    f = requests.get(url)
    bs = BeautifulSoup(f.text, 'lxml')
    a_list = bs.find_all('a')

    for a in a_list:
        href = 'http://www.phei.com.cn' + a['href']
        book_name = a.text.strip()

        if 'wssd_content.jsp?bookid' in href and book_name != '':
            #print text, href
            page_info = get_page_data(href)
            if not page_info: continue

            page_info[u'书名'] = book_name
            page_info['URL'] = href
            page_info_list.append(page_info)


#保存
wb = xlwt.Workbook()
sheet = wb.add_sheet(u'图书信息')

#头部
for i in range(0, len(page_info_keys)):
    sheet.write(0, i, page_info_keys[i])

for i in range(1, len(page_info_list)):
    page_info = page_info_list[i]

    for j in range(0, len(page_info_keys)):
        key = page_info_keys[j]
        content = page_info.get(key)
        #print content
        sheet.write(i, j, content)

#内容

wb.save(u'图书信息.xls')

print 'Done'
