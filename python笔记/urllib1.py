# coding:utf-8
from urllib import request

# get
url = 'https://api.douban.com/v2/book/2129650'
with request.urlopen(url) as f:
    data = f.read()
    print('status:', f.status, f.reason)
    for k, v in f.getheaders():
        print(k,'=',v)
    print('data=', data.decode('utf-8'))

# 模拟浏览器
req = request.Request('http://www.douban.com')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print(f.read().decode('utf-8'))

# POST
from urllib import parse
email = 'xushaoxun1209@qq.com'
password = 'psd'
login_data = parse.urlencode([
    ('email', 'xushaoxun1209@qq.com'),
    ('username', 'xushaoxun')
])
req = request.Request('http://httpbin.org/post')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('status=', f.status, f.reason)
    print(f.read().decode('utf-8'))