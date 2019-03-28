import unittest
from http_request.http_request import HttpRequest
from utils.do_excel.do_excel import DoExcel
from utils.case_conf.case_conf import GetConf
from ddt import ddt,data,unpack

@ddt
class RegisterTestCase(unittest.TestCase):
    register_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/register'

    @data(*register_case_list)
    def test_register_api(self,case):
        print(case['case_title'])
        response = HttpRequest(url = self.register_url, data=eval(case['case_data']), cookies=None).request_post()
        DoExcel('../utils/do_excel/test_case.xlsx','register',row = case['case_id'],value = response.json()['code']).set_value()
        print(response.json())
        self.assertEqual(str(case['case_expected']),response.json()['code'])
