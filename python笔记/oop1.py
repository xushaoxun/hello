# coding:utf-8

class Student():
    version = 'v1.1'    # 类属性，可以通过Student.version或者实例对象访问

    def __init__(self, name=None, score=0):
        self.__name = name      # Python3 中私有变量以__开头
        self.__score = score

    def print_scrore(self):
        print(self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


class Animal():
    def run(self):
        print('Aminal run')

class Dog(Animal):
    def run(self):
        print('Dog run')

class Timer():
    def run(self):
        print('timer run')

# 注意这个obj接受有run函数的对象
def run(obj):
    obj.run()

#首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。
def readImg(o):
    if hasattr(o, 'read'):
        return readData(o)
    return None


if __name__ == '__main__':
    print(Student.version)
    print(Student().version)

    run(Animal())
    run(Dog())
    run(Timer())

    o = Animal()
    print(isinstance(Dog(), Animal))

    # type返回对应的Class类型
    import types
    print(type(abs) == types.BuiltinFunctionType)   # True

    print(dir(o))   # 类似__xxx__的属性和方法在Python中都是有特殊用途的

    if hasattr(o, 'eat'):
        print('i can eat')

    r = getattr(o, 'run', None) # 如果attr没有可以返回默认值

'''
__slots__
'''
class Manager():
    __slots__ = ['name', 'age'] #这里有定义时才可以扩展属性

o = Manager()
o.name = 'eagle'
o.age = 25
#o.job = 'a' # error

class Dog():

    @property
    def birth(self):
        '''d.birth'''
        print('get birth')
        return self._birth

    @birth.setter
    def birth(self, value):
        '''d.birth = '''
        print('set birth')
        # 这里可以实现value检查
        self._birth = value

    @property
    def age(self):
        '''只读'''
        return 2015 - self._birth

d = Dog()
d.birth = 1990
print(d.birth)
print(d.age)

'''多重继承,类似java中extend一个类，implement多个类，实现接口。但python允许多重继承'''

'''定制类'''
class Dog():
    def __str__(self):
        return 'A Dog'

    def __getattr__(self, item):
        '''调用不存在的属性时会用这个方法'''
        if item == 'name':
            return 'no name'
        if item == 'age':
            return lambda :25

    # 实例对象可以被调用. 可以用callable判断
    def __call__(self, *args, **kwargs):
        print('i am callable')


d = Dog()
print(d.name)
print(d.birth)  # None
print(d.age())
d()
print(callable(d))

'''枚举类'''
from enum import Enum, unique
month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(month.Jan)    # Month.Jan
for name, member in month.__members__.items():
    print(name, member)

@unique # 检查没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Sun)          #Weekday.Sun
print(Weekday.Mon.value)    # 1
