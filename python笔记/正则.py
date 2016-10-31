# coding:utf-8
import re

# 强烈建议使用Python的r前缀，就不用考虑转义的问题了

# match
test = r'(\d{4})-(\d{2})-(\d{2})'
m = re.match(test, '2016-12-05')    # match从头匹配
if m:
    print(m.group())
    print(m.groups())

# seach
m = re.search(test, 'today is 2016-10-31. tomorrow is 2016-11-01')
if m:
    print(m.group())
    print(m.groups())

# findall
all = re.findall(test, 'today is 2016-10-31. tomorrow is 2016-11-01')
print(all)  # [('2016', '10', '31'), ('2016', '11', '01')]

email_patten = r'[\w\d]+@[\w\d]+\.(com|org|cn)'
email = 'someone@gmail.com'
m = re.match(email_patten, email)
if m:
    print(m.group(), m.groups())

# splic
s = 'root:x:0:0::/usr/bin/bash'
print(s.split(':'))
print(re.split(r':+', s))

s = 'Hello, hello, hEllo'
print(re.sub(r'hello', 'Hello', s, flags=re.IGNORECASE))

'''
贪婪模式
如果用到通配字符，默认会抓取尽可能多的字符串
可以用?放在* +后面
'''
s = 'my room # 302-5-9'
print(re.search(r'.+(\d+-\d-\d)', s).group(1))    # 2-5-9
print(re.search(r'.+?(\d+-\d-\d)', s).group(1))    # 302-5-9