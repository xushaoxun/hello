# coding:utf-8

'''
string -> decode成unicode储存 -> encode(utf-8)显示

从网络上取得的内容，要print出来，必须decode成unicode
urllib.request(url).read().decode('utf-8')
'''
'''
Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了
UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节
在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码
浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器

由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
Python对bytes类型的数据用带b前缀的单引号或双引号表示
以Unicode表示的str通过encode()方法可以编码为指定的bytes
'''
print('ABC')
print('ABC'.encode('utf-8'))    #b'ABC'
print('中'.encode('utf-8'))

'''
如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
'''
print(b'ABC'.decode('utf-8'))

