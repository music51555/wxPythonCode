import unittest
from test_cases.login_testcase import RegTestCase
from utils.do_excel.do_excel import DoExcel
import HTMLTestRunner
import sys,os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

case_list = DoExcel('../utils/do_excel/test_case.xlsx','login').get_value()

suite = unittest.TestSuite()

for case in case_list:
    suite.addTest(RegTestCase('test_reg_api',case['case_data'],case['case_expected']))

with open('../test_result/result.html','wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,
                                           title='注册模块测试用例')
    runner.run(suite)