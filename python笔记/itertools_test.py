# coding:utf-8
import itertools

# 不停顿
j = 1
for i in itertools.count(1):
    j += 1
    print(i)
    if j>100:
        break

j = 1
c = itertools.cycle('abc')
for i in c:
    j += 1
    print(i)
    if j>100:
        break

for i in itertools.repeat('hello', 3):
    print(i)

for i in itertools.chain('abc', 'ABC'):
    print(i)