import unittest
from unittest.calc_test_cases import ADDMthodTestCase
import HTMLTestRunner

suite = unittest.TestSuite()

# suite.addTest(ADDMthodTestCase('test_int_add'))
# suite.addTest(ADDMthodTestCase('test_two_zero_add'))

loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(ADDMthodTestCase))
# suite.addTest(loader.loadTestsFromModule(calc_test_cases))
suite.addTest(loader.loadTestsFromTestCase(ADDMthodTestCase))


with open('test_result.html','wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2,
                                           description='测试报告描述',
                                           title='calc测试报告')
    runner.run(suite)