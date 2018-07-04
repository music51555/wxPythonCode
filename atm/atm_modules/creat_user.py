import json,time

from atm_modules.login_account import login
from log import logger

def creat_user():
    f = open('../account/credit_info.json', 'r',encoding = 'utf-8')
    credit_info = json.load(f)
    f.close()

    card_ids = list(credit_info.keys())

    while True:
        name = input('请输入您的真实姓名：')
        pwd = input('请设置密码：')
        confim_info = input('请核对您的姓名和密码姓名：\n姓名：%s\n密码：%s\n确认请按y，重新输入请按b' % (name, pwd))

        if confim_info.lower() == 'y':
            new_id = int(card_ids[-1]) + 1
            credit_info[new_id] = {"name":name, "limit":15000, "pwd":pwd,"status":"useable"}

            f = open('../account/credit_info.json', 'w',encoding = 'utf-8')
            json.dump(credit_info,f,ensure_ascii = False)
            f.close()

            print('\033[0;31;42m申请成功,请牢记您的卡号%s,在ATM主页面登出当前用户后，可使用新的用户登录至系统\033[0m'%new_id)
            logger.logger.info('%s银行卡号被注册'%new_id)
            return
        else:
            continue

def freeze_user(credit_card_id):
    print('\033[0;31m您正在申请冻结账户，账户一旦被冻结，将不可登录，如需登录请联系管理员\033[0m')
    freeze_u = input('\033[0;31;42m确认冻结，请按y,返回请按b>>>\033[0m')

    if freeze_u.lower() == 'y':
        f = open('../account/credit_info.json', 'r', encoding='utf-8')
        credit_info = json.load(f)
        f.close()

        credit_info[credit_card_id]['status'] = 'freeze'
        f = open('../account/credit_info.json', 'w', encoding='utf-8')
        json.dump(credit_info,f,ensure_ascii = False)
        f.close()
        print('\033[0;31;42m账户冻结成功,登出后生效\033[0m')
        logger.logger.info('%s账户冻结成功'%credit_info[credit_card_id]['name'])
        return
    else:
        return

@login
def system_md(credit_card_id):
    print('欢迎您使用ATM系统管理功能,')
    while True:
        print('1. 申请信用卡\n2. 冻结账户')
        systen_md_num = input('请选择您要执行的系统功能序号>>>')

        if systen_md_num.isdigit():
            systen_md_num = int(systen_md_num)

            if systen_md_num in [1,2]:
                if systen_md_num == 1:
                    creat_user()
                    print('正在返回ATM主页...')
                    time.sleep(2)
                    return

                if systen_md_num == 2:
                    freeze_user(credit_card_id)
                    print('正在返回ATM主页...')
                    time.sleep(2)
                    return

            else:
                print('\033[0;31m您输入的功能序号不存在，请重新输入\033[0m')
                continue

        else:
            print('\033[0;31m您输入的功能序号不存在，请重新输入\033[0m')
            continue
