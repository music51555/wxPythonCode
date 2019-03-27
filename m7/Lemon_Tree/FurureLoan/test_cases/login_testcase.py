import unittest
from http_request.http_request import HttpRequest
from utils.do_cookies.set_cookies import SetCookies
from utils.do_excel.do_excel import DoExcel
from utils.case_conf.case_conf import GetConf
from ddt import ddt,data,unpack

mode = GetConf('../conf/conf.ini','LOGIN','case_id_list').get_conf()
login_case_list = DoExcel('../utils/do_excel/test_case.xlsx','login',mode=mode).get_value()

@ddt
class LoginTestCase(unittest.TestCase):
    register_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'

    @data(*login_case_list)
    def test_login_api(self,case):
        print(case['case_title'])
        response = HttpRequest(url = self.register_url,data=eval(case['case_data']), cookies=None).request_post()
        print(response.json())
        DoExcel('../utils/do_excel/test_case.xlsx','login',row = case['case_id'],value = response.json()['code']).set_value()
        if response.json()['code'] == '10001':
            setattr(SetCookies,'cookies',response.cookies)
        self.assertEqual(str(case['case_expected']),response.json()['code'])




