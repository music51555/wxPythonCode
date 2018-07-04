import time,json

from log import logger

logins = False
credit_card_id_bk = ''

def login(func):
    def verify_account(credit_card_id):
        count = 0
        while True:
            global logins
            global credit_card_id_bk

            if logins == False:
                print('\033[0;31;42m请先登录：\033[0m')
                credit_card_id = input('请输入您的信用卡卡号：')
                credit_card_pwd = input('请输入您的信用卡密码：')

                f = open('../account/credit_info.json', 'r',encoding = 'utf-8')
                credit_info = json.load(f)
                credit_card_id_bk = credit_card_id

                if credit_card_id in credit_info.keys() and credit_card_pwd == credit_info[credit_card_id]['pwd']:
                    if credit_info[credit_card_id]['status'] == 'useable':
                        logins = True
                        print('验证成功,请稍等,正在连接信用卡中心...')
                        logger.logger.info('%s用户登录'%credit_info[credit_card_id]['name'])
                        time.sleep(2)
                        func(credit_card_id)
                        return
                    else:
                        print('\033[0;31m对不起，您的账户被冻结,请联系管理员,即将返回...\033[0m')
                        time.sleep(2)
                        return
                else:
                    print("\033[0;31m您的信用卡卡号或密码输入错误，请重新输入：\033[0m")
                    count += 1
                    if count >= 3:
                        logger.logger.warning('用户累计输入密码%s次,存在可疑操作，请管理员注意' % count)
                    continue

            if logins == True:
                func(credit_card_id_bk)
                return

    return verify_account