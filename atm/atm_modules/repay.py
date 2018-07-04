import json,time

from atm_modules.login_account import login
from log import logger

f = open('../account/credit_info.json', 'r', encoding='utf-8')
credit_info = json.load(f)
f.close()

@login
def repay(credit_card_id):
    print('\033[0;31;42m欢迎使用ATM还款功能\033[0m')

    while True:
        repay_limit = input('请输入您要还款的金额,返回请按b>>>：')

        if repay_limit == 'b':
            break

        if repay_limit.isdigit():
            repay_limit = int(repay_limit)

            if repay_limit > 10000:
                print('\033[0;31m抱歉，系统设定单次还款金额在10000元以内\033[0m')
                continue

            elif repay_limit > 0:
                confirm_repay = input('\033[0;31;42m您要还款的金额是%s，确认请按y，取消转账请按b\33[0m'%repay_limit)
                if confirm_repay.lower() == 'y':
                    credit_info[credit_card_id]['limit'] += repay_limit
                    f = open('../account/credit_info.json', 'w', encoding='utf-8')
                    json.dump(credit_info, f, ensure_ascii=False)
                    f.close()
                    print('\033[0;31;42m还款成功，您稍后可在ATM主页中使用查询余额功能，查看您的账户余额\033[0m')
                    logger.logger.info('用户执行还款成功，还款金额%s'%repay_limit)
                    time.sleep(2)
                    return
                else:
                    return

            else:
                print('\033[0;31m抱歉，您输入的数据不合法，请重新输入\033[0m')

        else:
            print('\033[0;31m抱歉，您输入的数据不合法，请重新输入\033[0m')