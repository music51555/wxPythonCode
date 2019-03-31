from utils.case_conf.case_conf import GetConf
from settings import CONF_INI
from utils.do_mysql import DoMysql


def get_amount(mobilephone):
    print(mobilephone)
    amount = DoMysql().execute_sql('select LeaveAmount from member where MobilePhone = {}'.format(mobilephone))
    return amount

if __name__ == '__main__':
    print(get_amount(18012345678))