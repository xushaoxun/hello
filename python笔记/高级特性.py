# coding:utf-8

'''
两种方法
g = (x for x ing range(10))

def gen():
	yield 1
	yield 2
	yield 3
	yield 4
	yield 5
g = gen()	#g是一个生成器

可以用next(g)调用，直到StopIteration
调用方法一样
for i in g:
	print i
'''

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n += 1
f = fib(5)
for i in f:
	print i

'''
可迭代对象
1:list, tuple, set, string, dict
2:generator
直接作用于for循环的对象统称为可迭代对象：Iterable

用isinstance判断
'''

from collections import Iterable, Iterator
print isinstance(f, Iterable)	#True
print isinstance([], Iterable)	#True


'''Iterator对象表示的是一个数据流，
Iterator对象可以被next()函数调用并不断返回下一个数据，
直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，
但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
'''
print isinstance(f, Iterator)	#True
print isinstance([], Iterator)	#False
#next([1,2,3])	#会出错，因为list等不是Iter

#通过 iter()将Iterable转成Iterator
iterator = iter(range(10))

