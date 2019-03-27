import unittest
from test_cases.login_testcase import LoginTestCase
from test_cases.register_testcase import RegisterTestCase
from test_cases.recharge_testcase import  RechargeTestCase
import HTMLTestRunner
import sys,os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))
suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))
suite.addTest(loader.loadTestsFromTestCase(RechargeTestCase))

with open('../test_result/result.html','wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,
                                           title='登录模块测试用例')
    runner.run(suite)