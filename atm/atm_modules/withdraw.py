import json

from atm_modules.login_account import login

@login
def withdraw(credit_card_id):
    while True:
        withdraw_limit = input('欢迎使用ATM提现功能，请输入提取的金额,,返回ATM主页请按b>>>')

        if withdraw_limit.isdigit():
            withdraw_limit = int(withdraw_limit)
            f = open('../account/credit_info.json', 'r',encoding = 'utf-8')
            credit_info = json.load(f)

            if withdraw_limit <= credit_info[credit_card_id]['limit']:
                credit_info[credit_card_id]['limit'] -= withdraw_limit
                f = open('../account/credit_info.json','w',encoding = 'utf-8')
                json.dump(credit_info,f)
                print('\033[0;31;42m取现成功\033[0m')
                f.close()
            else:
                print('\033[0;31m抱歉，您提取的额度超出了您的信用额度，您当前的信用额度是%s,请重新输入要提取的金额\033[0m'%credit_info[credit_card_id]['limit'])
                continue
            f.close()

        elif withdraw_limit == 'b':
            return

        else:
            print('\033[0;31m抱歉，您的输入有误，请重新输入\033[0m')
            continue