# coding:utf-8

with open('OOP.py', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

# StringIO
from io import StringIO
with StringIO("hello\nworld") as s:
    for line in s:
        print(line)

print('内容'.encode('utf-8'))

# os
import os
print(os.name)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))

print(os.path.join('/home/user', '/name'))  # 这个对于不同操作系统不一样
print(os.path.split('/home/user/program'))  # ('/home/user', 'program')
print(os.path.splitext('/home/user/file.txt'))  #('/home/user/file', '.txt')用来取得扩展名

os.rename('OOP.py', 'oop.py')

# os.remove('file.txt')
os.mkdir('test')
os.rmdir('test')


#复制文件
import shutil
shutil.copy('oop.py', 'oop1.py')

print([x for x in os.listdir('..') if os.path.splitext(x)[1] == '.sh'])

print('-'*20)
def find(name):
    for i in os.listdir(os.curdir):
        if i.find(name) >= 0:
            print(i)
find('oo')

# 把变量从内存中变成可存储或传输的过程称之为序列化。在Python中叫pickling
import pickle
d = dict(name='eagle', age=35)
bytes = pickle.dumps(d) # 把任意对象序列化成一个bytes
#或者直接放进文件
f = open('d.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('d.txt', 'rb')
o = pickle.load(f)
print(o)

# josn
import json
j= (json.dumps(d))    # 将对象转成json字符串
o = json.loads(j)
print(type(o))

# json dump object
class Student():
    def __init__(self, name):
        self.name = name
s = Student('bob')
json.dumps(s,)


