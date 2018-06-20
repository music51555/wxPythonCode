import json,time

from atm_modules.login_account import login
from log import logger

@login
def transfer(credit_card_id):
    back = False
    print('\033[0;31;42m欢迎使用ATM转账功能\033[0m')

    while True:
        if back == True:
            break

        transfer_to = input('请输入对方的银行卡账号,退出请按b>>>：')

        if transfer_to == 'b':
            return

        f = open('../account/credit_info.json', 'r', encoding='utf-8')
        credit_info = json.load(f)
        f.close()

        if transfer_to in credit_info.keys():

            while True:
                if back == True:
                    break

                name = input("请核实账户姓名：")

                if name == credit_info[transfer_to]['name']:
                    while True:
                        transfer_limit = input('请输入转账金额：')
                        if transfer_limit.isdigit():
                            transfer_limit = int(transfer_limit)

                            if transfer_limit <= credit_info[credit_card_id]['limit']:
                                confirm_transfer = input(
                                    '\033[0;31;42m您要将%s元,转账至%s名下的%s银行卡号，确认请按y,取消转账请按b>>>\033[0m' % (transfer_limit, name, transfer_to))

                                if confirm_transfer.lower() == 'y':
                                    print('正在连接信用卡中心，请稍等...')
                                    credit_info[transfer_to]['limit'] += transfer_limit
                                    credit_info[credit_card_id]['limit'] -= transfer_limit
                                    f.close()

                                    f = open('../account/credit_info.json','w',encoding = 'utf-8')
                                    json.dump(credit_info,f,ensure_ascii = False)
                                    f.close()

                                    time.sleep(2)
                                    print('\033[0;31;42m转账成功,正在返回ATM主页...\033[0m')
                                    logger.logger.info('用户执行了转账操作,转账%s元，至%s账户'%(transfer_limit,transfer_to))
                                    time.sleep(2)
                                    return
                                else:
                                    back = True
                                    break

                            else:
                                print('\033[0;31m很抱歉，您转账的金额超过了您的信用额度，请当前的信用额度是%s，请重新输入转账金额\033[0m' % credit_info[credit_card_id]['limit'])
                                continue

                else:
                    print('\033[0;31m很抱歉，您输入的姓名和银行卡号不匹配，请重新输入\033[0m')
                    continue

        else:
            print('\033[0;31m您输入的银行卡号不存在，请重新输入\033[0m')
            continue