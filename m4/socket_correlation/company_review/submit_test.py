# import requests
# from concurrent.futures import ThreadPoolExecutor
#
# def task(url):
#     print('getting %s'%url)
#     response = requests.get(url)
#     return {'url':url,'html_text':response.text}
#
# def get_size(url_dict):
#     print('%s size is %s'%(url_dict['url'],len(url_dict['html_text'])))
#
# if __name__ == '__main__':
#     url_list = ['https://www.baidu.com',
#                 'http://www.qq.com',
#                 'http://www.python.org']
#     t = ThreadPoolExecutor(2)
#     for i in url_list:
#         res = t.submit(task,i).result()
#         get_size(res)

import requests
from concurrent.futures import ThreadPoolExecutor

def task(url):
    print('getting %s'%url)
    response = requests.get(url)
    return {'url':url,'html_text':response.text}

def get_size(url_obj):
    url_dict = url_obj.result()
    print('%s size is %s'%(url_dict['url'],len(url_dict['html_text'])))

if __name__ == '__main__':
    url_list = ['https://www.baidu.com',
                'http://www.qq.com',
                'http://www.python.org']
    t = ThreadPoolExecutor(2)
    for i in url_list:
        t.submit(task,i).add_done_callback(get_size)


