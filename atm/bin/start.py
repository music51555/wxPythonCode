import json,os,sys,time

atm_path = os.path.dirname(os.getcwd())
sys.path.append(atm_path)

from atm_modules import shopping_cart,account_book,withdraw,creat_user,transfer,repay,check_limit
from log import logger
logger.logger.info('ATM系统开始运行')

f = open('../account/credit_info.json','r',encoding = 'utf-8')
credit_info = json.load(f)

def welcome():
    credit_card_id = ''
    while True:
        print('欢迎光临\033[0;31;42mATM+购物商城\033[0m，请选择您要执行的功能序号：'.center(50, '~'))
        f = open('atm_main_modules.json', mode='r', encoding='utf-8')
        main_modules = json.load(f)
        for i in main_modules:
            print('%s\t%s' % (i, main_modules[i]))
        f.close()
        choice_md = input("请输入您要执行的功能序号>>>")
        if choice_md in main_modules.keys():

            if choice_md.isdigit():
                choice_md = int(choice_md)

            if choice_md == 1:
                print('请稍等，正在进入购物商城...')
                logger.logger.info('用户进入了购物商城')
                time.sleep(2)
                shopping_cart.shopping_cart(credit_card_id)

            if choice_md == 2:
                print('请稍等...')
                logger.logger.info('用户进入了提现功能')
                time.sleep(2)
                withdraw.withdraw(credit_card_id)

            if choice_md == 3:
                print('请稍等,正在进入转账系统...')
                logger.logger.info('用户进入了转账功能')
                time.sleep(2)
                transfer.transfer(credit_card_id)

            if choice_md == 4:
                print('请稍等，正在进入还款系统...')
                logger.logger.info('用户进入了还款功能')
                time.sleep(2)
                repay.repay(credit_card_id)

            if choice_md == 5:
                print('请稍等，正在打开记账本...')
                logger.logger.info('用户打开了记账本')
                time.sleep(2)
                account_book.account_book(credit_card_id)

            if choice_md == 6:
                print('请稍等，正在进入系统管理中心...')
                logger.logger.info('用户进入了系统管理中心')
                time.sleep(2)
                creat_user.system_md(credit_card_id)

            if choice_md == 7:
                print('请稍等，正在为您查询...')
                logger.logger.info('用户开始查询余额')
                time.sleep(2)
                check_limit.check_limit(credit_card_id)

            if choice_md == 8:
                logger.logger.info('用户退出了ATM系统')
                exit('感谢您的使用，再见，祝您生活愉快。')

        else:
            print('\033[0;31m您输入的功能序号不存在，请重新输入\033[0m')
            continue
welcome()