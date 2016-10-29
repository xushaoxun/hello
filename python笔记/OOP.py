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
