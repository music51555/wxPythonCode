import unittest
from qianchengdai.http_request import HTTPRequest
import re
from qianchengdai import get_cookies

class LoginTestCase(unittest.TestCase):
    def __init__(self,methodName,url,data,cookie,expect):
        super().__init__(methodName)
        self.url = url
        self.data = data
        self.cookie = cookie
        self.expect = expect

    def test_right_u_right_p(self):
        response = HTTPRequest(url=self.url,data=self.data).request_post()
        if response.cookies:
            setattr(get_cookies.GetCookies,'cookies',response.cookies)
        self.assertEqual(self.expect,re.search('登录成功',response.text).group())

    def test_right_u_error_p(self):

        response = HTTPRequest(url=self.url,data=self.data).request_post()
        self.assertEqual(self.expect,re.search('帐号或密码错误!',response.text).group())

    def test_empty_u_have_p(self):

        response = HTTPRequest(url=self.url,data=self.data).request_post()
        self.assertEqual(self.expect,re.search('此账号没有经过授权，请联系管理员!',response.text).group())

    def test_have_u_empty_p(self):
        data = {
            'phone':'18611848257',
            'password':'',
            'vcode':'',
            'remember_me':'1',
            'notify_url':''
        }

        response = HTTPRequest(url=self.url,data=data).request_post()
        # try:
        self.assertEqual('请输入密码!1',re.search('请输入密码!',response.text).group())
        # except AssertionError as e:
        #     raise ValueError(e)


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