# coding:utf-8

# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的摘要digest
import hashlib
md5 = hashlib.md5()
md5.update('hello'.encode('utf-8'))
md5.update('world'.encode('utf-8'))
print(md5.hexdigest())

# 别的算法步骤也类似
'''
由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
'''

def get_md5(password):
    md5 = hashlib.md5()

    md5.update((password + 'the Salt').encode('utf-8'))
    return md5.hexdigest()

print(get_md5('1234'))