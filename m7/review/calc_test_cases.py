import unittest
from calc import Calc

class TestCalcAdd(unittest.TestCase):

    def test_add_int(self):
        res = Calc(1,2).add()
        print('1+2的结果是:',res)
        self.assertEqual(2,res,msg='运算出错')

    def test_add_two_zero(self):
        print('0+0的结果是:',Calc(0,0).add())

    def test_add_minus(self):
        print('-1+-2的结果是：',Calc(-1,-2).add())

class TestCalcMulti(unittest.TestCase):

    def test_multi_int(self):
        print('1*2的结果是:',Calc(1,2).multi())

    def test_multi_two_zero(self):
        print('0*0的结果是:',Calc(0,0).multi())

    def test_multi_minus(self):
        print('-1*-2的结果是：',Calc(-1,-2).multi())

if __name__ == '__main__':
    unittest.main()