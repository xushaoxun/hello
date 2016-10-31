# coding:utf-8
try:
    print(1)
except BaseException as e:  # BaseException是所有错误的父类
    print(2)
finally:
    pass

# 调试，一般用print
a = 1
print(a)

#用print的地方，可以用assert
assert a==1, 'a != 1'

#logging
import logging
logging.basicConfig(level=logging.INFO)
logging.log(logging.INFO, 'some message')

# 单元测试
import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        print('setup stuff')

    def test_int(self):
        self.assertEqual(1, 1)

    def test_2(self):
        self.assertTrue(1==2)

    def tearDown(self):
        print('tear down stuff')

# 运行单元测试
if __name__ == '__main__':
    unittest.main()

# 或者用python -m unittest xx.py