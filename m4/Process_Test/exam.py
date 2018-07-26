#写一个程序，包含十个线程，子线程必须等待主线程sleep 10秒钟之后才执行，并打印当前时间
# from threading import Thread
# import time
#
# def task(name):
#     print('%s is running'%name)
#
# if __name__ == '__main__':
#     time.sleep(10)
#     print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
#     for i in range(10):
#         t = Thread(target = task,args = ('子进程%s'%i,))
#         t.start()
#     time.sleep(10)

#写一个程序，包含十个线程，同时只能有五个子线程并行执行
# from concurrent.futures import ThreadPoolExecutor
# import time
#
# def task(name):
#     time.sleep(1)
#     print('%s is running'%name)
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(5)
#     for i in range(10):
#         pool.submit(task,'alex')

#写一个程序，要求用户输入用户名和密码，要求密码长度不少于6个字符，
#且必须以字母开头，如果密码合法，则将该密码使用md5算法加密后的
#十六进制概要值存入名为password.txt的文件，超过三次不合法则退出程序
import string
import hashlib

count = 1
while True:
    username = input('请输入用户名:')
    password = input('请输入密码:')
    if count == 3:
        print('您的输入次数达到上限，程序结束')
    if len(password) < 6 or (password[0] not in list(string.ascii_lowercase)) and (password[0] not in list(string.ascii_uppercase)):
        print('密码不能少于6位,且必须以字母开头')
        count += 1
        continue
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    with open('password.txt','w') as f:
        f.write(m.hexdigest())