import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.YDMHTTP_UTILS import *

class Douban_Movie():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    proxies = {
        'http': '59.44.247.194:9797'
    }

    def __init__(self):
        self.session = requests.session()

    def request_index(self):

        index_url = 'https://accounts.douban.com/login'
        login_text = self.session.get(url=index_url, headers = self.headers).text

        return login_text

    def request_login(self, result):
        formdata = {
            'source': 'index_nav',
            'form_email': '18611848257',
            'form_password': 'nishi458',
            'captcha-solution': result,
            # 'captcha-id': 'UHV911bYtLDTa4odapTn8lXc:en',
        }

        login_url = 'https://accounts.douban.com/login'
        login_text = self.session.post(url = login_url, proxies = self.proxies, data=formdata, headers = self.headers).text

        self.save_self_page()

    def get_valid_img(self):

        login_text = self.request_index()
        soup = BeautifulSoup(login_text, 'lxml')

        valicode_img_url = soup.select('.captcha_image')[0]['src']

        valicode_img_content = requests.get(url = valicode_img_url, headers = self.headers).content

        with open('../utils/valid_img.png', 'wb') as f:
            f.write(valicode_img_content)

        self.yundama()

    def yundama(self):
        # 用户名
        username = 'music51555'

        # 密码
        password = 'nishi458_2'

        # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
        appid = 6535

        # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
        appkey = '0d9170626841d7fea4f1a0674f240616'

        # 图片文件
        filename = '../utils/valid_img.png'

        # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
        codetype = 3000

        # 超时时间，秒
        timeout = 60

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

    def save_self_page(self):
        self_index = 'https://www.douban.com/people/143360064/'

        self_index_text = self.session.get(url = self_index).text

        with open('self_index.html', 'w', encoding='utf-8') as f:
            f.write(self_index_text)

    def movie_rank(self):
        params = {
            'type': 24,
            'interval_id': '100:90',
            'action':'',
            'start': 0,
            'limit': 60
        }

        xiju_type_url = 'https://movie.douban.com/j/chart/top_list?'

        movie_list = list(self.session.get(url = xiju_type_url,params = params, headers = self.headers).json())

        print(movie_list)
        print(type(movie_list))

        for movie in list(movie_list):
            movie_name = movie['title']
            cover_url = movie['cover_url']
            movie_detail_url = movie['url']

            print(movie_name)
            print(cover_url)
            print(movie_detail_url)
    #
    # def movie_detail(self):
    #     self.session.get()

if __name__ == '__main__':
    douban = Douban_Movie()
    result = douban.get_valid_img()
    douban.request_login(result)
    douban.movie_rank()






