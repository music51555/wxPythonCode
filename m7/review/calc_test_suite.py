import unittest
from calc_test_cases import TestCalcAdd

suite = unittest.TestSuite()

# 将测试用例类中的测试用例逐一的添加到测试套件中，比较复杂，需要一条一条添加
suite.addTest(TestCalcAdd('test_add_int'))
suite.addTest(TestCalcAdd('test_add_minus'))
suite.addTest(TestCalcAdd('test_add_two_zero'))


loader = unittest.TestLoader()
# 加载用例方式一：加载测试类，将类中的所有测试用例加载到
suite.addTest(loader.loadTestsFromTestCase(TestCalcAdd))

# 加载用例方式二：加载测试用例的py文件，将里面所有测试类的测试用例添加到测试套件中
import calc_test_cases
suite.addTest(loader.loadTestsFromModule(calc_test_cases))

runner = unittest.TextTestRunner()
runner.run(suite)