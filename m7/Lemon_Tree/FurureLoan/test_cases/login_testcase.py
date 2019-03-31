import unittest
from http_request.http_request import HttpRequest
from utils.do_cookies.set_cookies import SetCookies
from utils.do_excel.pandans_test import DoExcel
from utils.case_conf.case_conf import GetConf
from ddt import ddt,data,unpack
from settings import EXCEL_FILE,CONF_INI
from log.log_recorder import LogRecorder
from services.get_amount import get_amount

case_list = DoExcel(EXCEL_FILE).get_case_list()
logger = LogRecorder()
mount_list = eval(GetConf(CONF_INI,'AMOUNT_ASSERT','amount_list').get_conf())

@ddt
class ModuleTestCase(unittest.TestCase):
    is_sucess = None

    @data(*case_list)
    def test_api(self,case):
        logger.info('当前执行的用例是{}'.format(case['case_title']))
        logger.info('请求的参数是{}'.format(case['case_data']))
        logger.info('当前请求的url是{}'.format(case['url']))

        if case['sheet_name'] in mount_list:
            print(eval(case['case_data']))
            amount = get_amount(eval(case['case_data'])['mobilephone'])
            logger.info('请求前的余额是{}'.format(amount))
            response = HttpRequest(
                url=case['url'],
                data=eval(case['case_data']),
                cookies=getattr(SetCookies,'cookies')).request_post()
        else:
            response = HttpRequest(
                url=case['url'],
                data=eval(case['case_data']),
                cookies=getattr(SetCookies, 'cookies')).request_post()
        if response.cookies:
            setattr(SetCookies, 'cookies', response.cookies)

        logger.info('当前用例执行的结果是{}'.format(response.json()))
        try:
            self.assertEqual(str(case['case_expected']),response.json()['code'])
            self.is_sucess = 'PASS'
            if case['sheet_name'] in mount_list:
                amount = get_amount(eval(case['case_data'])['mobilephone'])
                logger.info('请求后的余额是{}'.format(amount))
        except AssertionError as e:
            self.is_sucess = 'FAIL'
            raise e
        finally:
            DoExcel(EXCEL_FILE).update_result(case['sheet_name'],response.json(),case)
            DoExcel(EXCEL_FILE).update_success(case['sheet_name'],self.is_sucess,case)





