import unittest
from qianchengdai.app_test_cases import LoginTestCase
from qianchengdai.app_test_cases import AddBankCard
from qianchengdai.get_cookies import GetCookies
from qianchengdai.util.openpyxl_tools import DoExcel
import HTMLTestRunner

login_url = 'http://120.78.128.25:8765/Frontend/Index/login'

class QCDLoadTestCases:

    def get_suite(self):
        self.suite = unittest.TestSuite()

    def get_loader(self):
        self.loader = unittest.TestLoader()

    def login_testcases(self):
        case_list = DoExcel('util/testcase_data.xlsx','login').get_case_list()
        for case in case_list:
            self.suite.addTest(LoginTestCase(case['case_name'],
                                             login_url,
                                             eval(case['case_data']),
                                             getattr(GetCookies,'cookies'),
                                             case['case_expected']
                                             ))

    def start(self):
        self.get_suite()
        self.get_loader()
        self.login_testcases()
        with open('login.html','wb') as f:
            runner = HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2,
                                                   description='登录测试用例集',
                                                   title='登录模块测试报告')
            runner.run(self.suite)

if __name__ == '__main__':
    first_test = QCDLoadTestCases()
    first_test.start()