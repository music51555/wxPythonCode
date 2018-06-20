import time,json

from atm_modules.login_account import login

@login
def account_book(credit_card_id):
    f = open('../account/credit_info.json', 'r', encoding='utf-8')
    credit_info = json.load(f)
    f.close()

    print('请稍等，正在为您打印您的消费清单...')
    time.sleep(2)

    f = open('../atm_modules/%saccount_book.txt'%credit_info[credit_card_id]['name'],'r',encoding = 'utf-8')
    data = f.read()
    if len(data) > 0:
        for i in data:
            print(i,end = '')

        while True:
            back_menu = input('返回ATM主页，请按b>>>')
            if back_menu == 'b':
                print('正在跳转到ATM主页，请稍等...')
                time.sleep(2)
                return
            else:
                print('\033[0;31m您的输入有误，请重新输入\033[0m')
                continue
    else:
        print('\033[0;31m很抱歉，未查询到消费记录，正在返回ATM主页...\033[0m')
        time.sleep(2)
        return