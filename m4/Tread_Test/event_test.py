from threading import Event
from threading import Thread
import time

def conn(e):
    count = 1
    print('正在尝试连接服务器,%s'%count)
    e.wait()
    print('服务器连接成功')

def check(e):
    print('正在检查服务器')
    time.sleep(7)
    print('您现在可以连接了')
    e.set()

if __name__ == '__main__':
    e = Event()
    t1 = Thread(target = check,args = (e,))
    t2 = Thread(target = conn,args = (e,))
    t1.start()
    t2.start()