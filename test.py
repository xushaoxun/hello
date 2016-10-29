# coding:utf-8
'''doc'''

class Parent():
    def __init__(self):
		print 'call ' , self.__class__

class Child():
	def __init__(self):
		parent.__init__(self)
		print 'call ' , self.__class__

p = Parent()
c = Child()

class RoundFloatManual():
	def __init__(self, val):
		assert isinstance(val, float), 'Value must be a float'
		self.value = round(val, 2)

	def __str__(self):
		return '%.2f' % self.value

	__repr__ = __str__


r = RoundFloatManual(3.1)
print r

class Time60():
	def __init__(self, hour, minute):
		self.hour = hour
		self.minute = minute

	def __str__(self):
		return '%s:%s' % (self.hour, self.minute)


t1 = Time60(4, 50)
t2 = Time60(5, 50)
print t1, t2