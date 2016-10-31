# coding:utf-8

import base64
en = base64.b64encode(b'hello world')
print(en)
de = base64.b64decode(en)
print(de)