import json,time,os,subprocess

from atm_modules.login_account import login
from log import logger



@login
def shopping_cart(credit_card_id):
    shopping_cart = []
    back = False
    print('欢迎来到\033[0;31;42m购物商城\033[0m，我们为您准备了丰富的商品：'.center(50, '~'))

    while True:
        def product_list():
            f = open('../atm_modules/product_list.json', 'r', encoding='utf-8')
            products = json.load(f)

            for key in products:
                print(' %s：\t%s\t%s元' % (key, products[key][0], products[key][1]))

            while True:
                buy_num = input('请输入要购买的产品序号,将商品添加到购物车，返回商城主页，请按[b]>>>：')
                if buy_num == 'b':
                    break

                if buy_num in products.keys():
                    shopping_cart.append(products[buy_num])
                    print('\033[1;31;42m%s已被添加到购物车，价格\033[4;31;42m%s\033[1;31;42m元\033[0m' % (
                        products[buy_num][0], products[buy_num][1]))
                    continue
                else:
                    print('\033[0;31m您输入的商品序号不存在，请重新输入\033[0m')
                    continue

        while True:
            print('1、打印商品列表\n2、购物车结算')
            choice_md = input('请输入您要执行的功能序号,返回ATM主页请按b>>>')
            if choice_md.isdigit():
                choice_md = int(choice_md)

                if choice_md in [1, 2]:
                    if choice_md == 1:
                        print('\033[0;31;42m商品列表:\033[0m')
                        product_list()

                    if choice_md == 2:
                        if bool(shopping_cart):
                            count = 0
                            sum = 0
                            print('\033[0;31;42m您的购物车中有:\033[0m')

                            for i, v in enumerate(shopping_cart):
                                print('%s.\t%s\t%s元' % (i + 1, shopping_cart[i][0], shopping_cart[i][1]))
                                sum += shopping_cart[i][1]
                            print('\033[0;31;42m共计消费%s元\033[0m' % sum)

                            while True:
                                if back == True:
                                    break

                                settle_accounts = input('确认结算请按y，返回商城主页请按b>>>')

                                if settle_accounts in ['y', 'b']:
                                    if settle_accounts.lower() == 'y':

                                        while True:
                                            credit_card_id = input('请输入您的信用卡卡号：')
                                            credit_card_pwd = input('请输入您的信用卡密码：')
                                            f = open('../account/credit_info.json', 'r',encoding = 'utf-8')
                                            credit_info = json.load(f)

                                            if credit_card_id in credit_info.keys() and credit_card_pwd == \
                                                    credit_info[credit_card_id]['pwd']:
                                                print('验证成功,请稍等,正在连接信用卡中心...')
                                                time.sleep(2)

                                                if sum <= credit_info[credit_card_id]['limit']:
                                                    credit_info[credit_card_id]['limit'] = \
                                                        credit_info[credit_card_id]['limit'] - sum
                                                    print(
                                                        '\033[0;31;42m购买成功,您还可以使用ATM主页功能中的【记账本】功能，浏览您的消费记录，正在返回购物商城主页...\033[0m')
                                                    logger.logger.info('用户在购物商城成功消费%s元'%sum)
                                                    f.close()

                                                    f = open('../account/credit_info.json', 'w',encoding = 'utf-8')
                                                    json.dump(credit_info, f)
                                                    f.close()

                                                    if os.path.exists('../atm_modules/%saccount_book.txt'%credit_info[credit_card_id]['name']) == False:
                                                        if os.name == 'nt':
                                                            subprocess.run('mkdir %s.txt'%credit_info[credit_card_id]['name'],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
                                                        if os.name == 'posix':
                                                            subprocess.run('touch %s.txt'%credit_info[credit_card_id]['name'],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
                                                    else:
                                                        pass

                                                    f = open('../atm_modules/%saccount_book.txt'%credit_info[credit_card_id]['name'], 'r+',
                                                             encoding='utf-8')
                                                    data = f.read()
                                                    line_num = data.count('\n')

                                                    for i, v in enumerate(shopping_cart):
                                                        account_book_record = '%s\t' % (
                                                                line_num + 1) + time.strftime(
                                                            '%Y-%m-%d %H:%M:%S') + '\t购买了\t' + '%s\t%s元\n' % (
                                                                                  shopping_cart[i][0],
                                                                                  shopping_cart[i][1])
                                                        line_num += 1
                                                        f.write(account_book_record)
                                                    f.close()

                                                    time.sleep(2)
                                                    back = True
                                                    break

                                                else:
                                                    print(
                                                        '\033[0;31m对不起，您的账户余额不足\033[0m\n温馨提示：您可以使用ATM主页中的还款功能，保证您的余额充足后再次购买，感谢您的使用。')
                                                    print('\033[0;31;42m正在返回购物商城主页...\033[0m')
                                                    time.sleep(2)
                                                    back = True
                                                    break

                                            else:
                                                print("\033[0;31m您的信用卡卡号或密码输入错误，请重新输入：\033[0m")
                                                count += 1

                                                if count > 2:
                                                    logger.logger.warning('用户累计输入密码%s次,存在可疑操作，请管理员注意'%count)
                                                continue

                                    if settle_accounts.lower() == 'b':
                                        break

                                else:
                                    print('\033[0;31m您的输入有误，请重新输入\033[0m')
                                    continue

                        else:
                            print('\033[0;31;42m您的购物车还是空的哦~快去购买您喜爱的商品吧\033[0m')
                            continue

                else:
                    print('\033[0;31m您输入的功能序号不存在，请重新输入\033[0m')
                    continue

            elif choice_md == 'b':
                f = open('../account/credit_info.json', 'r', encoding='utf-8')
                credit_info = json.load(f)
                f.close()
                logger.logger.info('%s用户退出了购物商城'%credit_info[credit_card_id]['name'])
                return

            else:
                print('\033[0;31m对不起，您输入的商品序号输有误，请重新输入\033[0m')
                continue