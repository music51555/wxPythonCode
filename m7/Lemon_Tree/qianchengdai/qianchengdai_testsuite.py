import unittest
from qianchengdai.app_test_cases import LoginTestCase
from qianchengdai.app_test_cases import AddBankCard
from qianchengdai.get_cookies import GetCookies
from qianchengdai.util.openpyxl_tools import get_value
import json
import re

login_url = 'http://120.78.128.25:8765/Frontend/Index/login'

class QCDLoadTestCases:

    def get_suite(self):
        self.suite = unittest.TestSuite()

    def get_loader(self):
        self.loader = unittest.TestLoader()

    def login_testcases(self):
        testcase_list = get_value()
        for testcase in testcase_list:
            self.suite.addTest(LoginTestCase(methodName=testcase['method_name'],
                                             url=login_url,
                                             data=eval(testcase['data']),
                                             cookie=getattr(GetCookies,'cookies'),
                                             expect=testcase['expect']))
        # self.suite.addTest(self.loader.loadTestsFromTestCase(LoginTestCase))
        # self.suite.addTest(self.loader.loadTestsFromTestCase(AddBankCard))

    def start(self):
        self.get_suite()
        self.get_loader()
        self.login_testcases()
        with open('login.txt','w',encoding='utf=8') as f:
            runner = unittest.TextTestRunner(stream=f,verbosity=2)
            runner.run(self.suite)

if __name__ == '__main__':
    first_test = QCDLoadTestCases()
    first_test.start()