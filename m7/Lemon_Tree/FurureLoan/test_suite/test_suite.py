import unittest
from test_cases.login_testcase import ModuleTestCase
import HTMLTestRunner
import HTMLTestRunnerNew
import sys,os
from settings import RESULT_FILE

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(ModuleTestCase))

with open(RESULT_FILE,'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,
                                           title='登录模块测试用例')
    runner.run(suite)
