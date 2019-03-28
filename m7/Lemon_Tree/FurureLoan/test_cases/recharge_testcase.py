import unittest
from http_request.http_request import HttpRequest
from utils.do_cookies.set_cookies import SetCookies
from utils.do_excel.do_excel import DoExcel
from ddt import ddt,data,unpack
from utils.case_conf.case_conf import GetConf

@ddt
class RechargeTestCase(unittest.TestCase):
    recharge_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'

    @data(*recharge_case_list)
    def test_recharge_api(self,case):
        print(case['case_title'])
        cookies = getattr(SetCookies,'cookies')
        response = HttpRequest(url=self.recharge_url,data=eval(case['case_data']), cookies=cookies).request_post()
        DoExcel('../utils/do_excel/test_case.xlsx','recharge',row = case['case_id'],value = response.json()['code']).set_value()
        print(response.json())
        self.assertEqual(str(case['case_expected']),response.json()['code'])