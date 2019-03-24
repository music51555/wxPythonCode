import unittest
from unittest.calc import Calc

class ADDMthodTestCase(unittest.TestCase):
    def test_int_add(self):
        res = Calc(1,2,).add()
        print('1+2 result{0}'.format(res))
        self.assertEqual(3,res,msg='计算错误')

    def test_two_zero_add(self):
        res = Calc(0,0).add()
        print('1+2 result{0}'.format(res))
        self.assertEqual(0,res)

if __name__ == '__main__':
    unittest.main()
