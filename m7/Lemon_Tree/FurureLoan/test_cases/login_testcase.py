import unittest
from http_request.http_request import HttpRequest
from utils.do_cookies.set_cookies import SetCookies
# from utils.do_excel.do_excel import DoExcel
from utils.do_excel.pandans_test import DoExcel
from ddt import ddt,data,unpack
from settings import EXCEL_FILE

case_list = DoExcel(EXCEL_FILE).get_case_list()

@ddt
class ModuleTestCase(unittest.TestCase):
    is_sucess = None

    @data(*case_list)
    def test_api(self,case):
        print(case['case_title'])
        response = HttpRequest(case['url'], data=eval(case['case_data']), cookies=getattr(SetCookies,'cookies')).request_post()
        print(response.json())
        if response.cookies:
            setattr(SetCookies,'cookies',response.cookies)
        try:
            self.assertEqual(str(case['case_expected']),response.json()['code'])
            self.is_sucess = 'PASS'
        except AssertionError as e:
            self.is_sucess = 'FAIL'
            raise e





