# coding:utf-8
'''参数
1.位置参数
2.默认参数
3.可变参数
4.关键字参数
'''
def fun(a, b, c=1, *args, **kwargs):
	print a, b, c
	print args
	print kwargs

fun(1, 2, 3, 4, 5)


'''
函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
'''
print map(lambda x:x*x, range(10))
print reduce(lambda x, y: x + y, range(10))

print filter(lambda s: s and s.strip(), ['abc', '', '  '])	# 去掉空串

sorted(['Abc', 'abc'], key=str.lower)

'''闭包
'''
def lazy_sum(*args):
	def f():
		s = 0
		for i in args:
			s += i
		return s
	return f
f = lazy_sum(1, 2, 3, 4)
print f()

'''装饰器
'''

import functools

def log(func):
	@functools.wraps(func)	#将func.__name__还原
	def wrapper(*args, **kwargs):
		print 'call %s' % func.__name__
		return func(*args, **kwargs)
	return wrapper

@log	#相当于now = log(now)
def now():
	print '2016-10-29'


now()


#带参数的decorator
def logger(level='info'):
	def decorator(func):
		def wrapper(*args, **kwargs):
			print 'LEVEL:%s %s' % (level, func.__name__)
			return func(*args, **kwargs)
		return wrapper
	return decorator

@logger('warn')
def hello(name):
	print 'hello, ', name
hello('shawn')


'''
偏函数functools.partial
当函数的参数个数太多，需要简化时，
使用functools.partial可以创建一个新的函数，
这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''
int2 = functools.partial(int, base=2)	#相当于int(xx, base=2)