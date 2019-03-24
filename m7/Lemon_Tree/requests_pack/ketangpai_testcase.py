import unittest
from requests_pack.http_request import HttpRequest

class KTPLoginTestCase(unittest.TestCase):
    def setUp(self):
        print('准备开始执行用例')

    def test_right_username_and_password(self):
        login_res = HttpRequest('18611848257','nishi458')\
            .request_post().json()
        self.assertEqual('success',login_res['info'])

    def test_right_username_and_error_password(self):
        login_res = HttpRequest('18611848257','nishi4581')\
            .request_post().json()
        self.assertEqual('success',login_res['info'])

    def tearDown(self):
        print('当前测试用例执行完毕')

if __name__ == '__main__':
    unittest.main()