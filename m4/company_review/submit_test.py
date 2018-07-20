from concurrent.futures import ThreadPoolExecutor
import time,random,requests,os

def task(url):
    print('getting %s, it is pid %s'%(url,os.getpid()))
    time.sleep(random.randint(1,5))
    response = requests.get(url)
    return {'url':url,'html_text':response.text}

def statistics(url_obj):
    url_dict = url_obj.result()
    print('%s size is %s'%(url_dict['url'],len(url_dict['html_text'])))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(2)
    url_list = ['https://www.baidu.com',
                'http://www.qq.com',
                'http://www.python.org']
    for i in url_list:
        pool.submit(task,i).add_done_callback(statistics)
