# import time,random
# from concurrent.futures import ThreadPoolExecutor
#
# def task(name):
#     print('%s is writing code'%name)
#     time.sleep(random.randint(1,3))
#     res = random.randint(1,15)
#     return {'name':name,'line':res}
#
# def check_code(future_obj):
#     code_dict = future_obj.result()
#     print('%s write %s line code'%(code_dict['name'],code_dict['line']))
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor()
#     pool.submit(task,'alex').add_done_callback(check_code)

from concurrent.futures import ThreadPoolExecutor
import requests

def task(url):
    print('viewing %s'%url)
    respone = requests.get(url)
    return {'url':url,'text':respone.text}

def check_url(url_obj):
    url_dict = url_obj.result()
    print('%s indexpage length is %s'%(url_dict['url'],len(url_dict['text'])))

if __name__ == '__main__':
    url_list = ['https://www.baidu.com',
                'http://www.qq.com',
                'http://www.python.org']
    pool = ThreadPoolExecutor(2)
    for url in url_list:
        pool.submit(task,url).add_done_callback(check_url)
        pool.submit(task,url).add_done_callback(check_url)
        pool.submit(task,url).add_done_callback(check_url)
        pool.submit(task,url).add_done_callback(check_url)
        pool.submit(task,url).add_done_callback(check_url)