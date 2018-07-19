from concurrent.futures import ThreadPoolExecutor
import requests

def get_url(url):
    print('getting %s'%url)
    response = requests.get(url)
    return {'url':url,'html_text':response.text}

def parser(url_obj):
    url_dict = url_obj.result()
    print('%s html text len %s'%(url_dict['url'],len(url_dict['html_text'])))

if __name__ == '__main__':
    url = ['https://www.baidu.com',
           'http://www.qq.com',
           'http://www.linuxprobe.com']
    executor = ThreadPoolExecutor(2)
    for i in url:
        executor.submit(get_url,i).add_done_callback(parser)