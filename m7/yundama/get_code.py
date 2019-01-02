from yundama.YDM3 import *

def get_valid_code(file_name):
    # 用户名
    username = 'music51555'

    # 密码
    password = 'nishi458_2'

    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid = 6535

    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey = '0d9170626841d7fea4f1a0674f240616'

    # 图片文件
    filename = file_name

    # 验证码识别类型 http://www.yundama.com/price.html
    codetype = 3000

    # 超时时间，秒
    timeout = 20

    # 检查
    if (username == 'username'):
        print('请设置好相关参数再测试')
    else:
        # 初始化
        yundama = YDMHttp(username, password, appid, appkey)

        # 登陆云打码
        uid = yundama.login();
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance();
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout);
        print('cid: %s, result: %s' % (cid, result))

        return result
