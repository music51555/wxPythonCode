import unittest
from qianchengdai.http_request import HTTPRequest
import re
from qianchengdai import get_cookies
from qianchengdai.util.openpyxl_tools import DoExcel
from ddt import ddt,data,unpack
from qianchengdai.util.get_conf import GetConf

button = GetConf('util/conf.ini','BUTTON','button').get_conf()
case_list = DoExcel('util/testcase_data.xlsx', 'login',button).get_case_list()

@ddt
class LoginTestCase(unittest.TestCase):

    login_url = 'http://120.78.128.25:8765/Frontend/Index/login'

    def setUp(self):
        print('开始测试')

    @data(*case_list)
    def test_login_api(self,testcase):
        print(testcase['case_desc'])
        response = HTTPRequest(url=self.login_url,data=eval(testcase['case_data'])).request_post()
        if response.cookies:
            setattr(get_cookies.GetCookies,'cookies',response.cookies)
        try:
            really = re.search(testcase['case_expected'],response.text).group()
        except AttributeError as e:
            raise e
        else:
            self.assertEqual(testcase['case_expected'],really)


class AddBankCard(unittest.TestCase):
    url = 'http://120.78.128.25:8765/Frontend/Member/addBankcard'

    def setUp(self):
        url = 'http://120.78.128.25:8765/Frontend/Index/login'

        data = {
            'phone': '18611848257',
            'password': 'nishi458',
            'vcode': '',
            'remember_me': '1',
            'notify_url': ''
        }

        self.response = HTTPRequest(url=url, data=data).request_post()


    def test_first_full_right_fill(self):
        data = {
            'hiddenBankCode': 'BJHR',
            'bankname': '北京怀柔融兴村镇银行',
            'banknumber': '6222 0222 0100 3738 129',
            'province': '北京',
            'city': '北京',
            'branchname': '北京支行'
        }
        response = HTTPRequest(url=self.url,data=data,cookies=self.response.cookies).request_post()
        self.assertEqual('添加成功',response.json()['msg'])


    def test_second_full_right_fill(self):
        data = {
            'hiddenBankCode': 'BJHR',
            'bankname': '北京怀柔融兴村镇银行',
            'banknumber': '6222 0222 0100 3738 129',
            'province': '北京',
            'city': '北京',
            'branchname': '北京支行'
        }
        response = HTTPRequest(url=self.url,data=data,cookies=self.response.cookies).request_post()
        self.assertEqual('该银行卡您已添加过，无需重复添加',response.json()['msg'])

if __name__ == '__main__':
    unittest.main()