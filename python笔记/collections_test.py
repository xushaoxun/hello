# coding:utf-8

# name tuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y']) #表示坐标的tuple
point = Point(1, 3)  # Point(x=1, y=3)
print(point.x, point.y)

print(isinstance(point, tuple)) # 创建的对象是tuple的子类

'''
deque
list是线性存储，数据量大的时候，插入和删除效率很低
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
'''
from collections import deque
dq = deque()
dq.append(1)
dq.append(2)
dq.appendleft(3)
print(dq)
dq.pop()
print(dq)

'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。
如果希望key不存在时，返回一个默认值，就可以用defaultdict：
'''
from collections import defaultdict
dd = defaultdict(lambda :None)
print(dd['a'])

'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict：
OrderedDict的Key会按照插入的顺序排列
'''
from collections import OrderedDict
od = OrderedDict({'a':1, 'b':2})
print(od)
print(od.keys())

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        assert capacity > 1, 'Capacity should > 0'
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = True if key in self else False

        if len(self) >= self._capacity:
            last = self.popitem(last=False)
            print('remove item ', last)

        OrderedDict.__setitem__(self, key, value)

lod = LastUpdatedOrderedDict(7)
for i in range(10):
    lod[i] = i+10
print(lod)

from collections import Counter
c = Counter([1, 2, 3, 4, 4])
print(c)