import unittest
from http_request.http_request import HttpRequest


class RegTestCase(unittest.TestCase):
    register_url = 'http://120.78.128.25:8765/futureloan/mvc/api/member/register'

    def __init__(self,methodName,data,expected):
        super().__init__(methodName)
        self.data = data
        self.expected = expected

    def test_reg_api(self):
        response = HttpRequest(url = self.register_url,data=self.data).request_get()
        print(response.text)
        print(response.json())
        self.assertEqual(self.expected,response.json())

# if __name__ == '__main__':
#     r = RegTestCase('test_reg_api','{"mobilephone":"18611848257","pwd":"nishi458","regname":"乐乐"}','10001')
#     r.test_reg_api()

{'phone':'13911228153',}
:
: aewy
code: 8989
password: nishi458
agree: on
