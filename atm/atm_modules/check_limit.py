import json,time

from atm_modules.login_account import login

@login
def check_limit(credit_card_id):
    f = open('../account/credit_info.json', 'r', encoding='utf-8')
    credit_info = json.load(f)
    f.close()

    print('\033[0;31;42m您的账户余额：%s元\033[0m'%credit_info[credit_card_id]['limit'])

    print('3秒后返回ATM主页...')
    time.sleep(3)
    return