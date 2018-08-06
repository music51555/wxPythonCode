from concurrent.futures import ThreadPoolExecutor
import time,requests

def view_html(url):
    response = requests.get(url)
    print('get %s'%url)
    return {url:url,'text':response.text}

def get_size(url_obj):
    print(len(url_obj.result()['text']))

if __name__ == '__main__':
    www_list = ['https://www.baidu.com',
                'http://www.qq.com',
                'http://www.sina.com',
                'http://www.python.org']
    pool = ThreadPoolExecutor(2)
    for i in www_list:
        pool.submit(view_html,i).add_done_callback(get_size)