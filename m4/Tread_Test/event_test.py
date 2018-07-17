import time
from threading import Thread,current_thread,Event

t = Event()

def conn():
    n = 0
    while not t.is_set():
        if n == 3:
            print('连接服务端失败')
            return
        print('%s 正在尝试连接服务端,%s次'%(current_thread().getName(),n))
        time.sleep(1)
        n += 1
        continue
    t.wait()
    print('%s 连接成功'%current_thread().getName())

def check():
    print('正在检查服务端连接...')
    time.sleep(2)
    print('您可以连接服务端了')
    t.set()

if __name__ == '__main__':
    t1 = Thread(target = check)
    t2 = Thread(target = conn,name = '客户端')

    t1.start()
    t2.start()