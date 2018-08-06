from threading import Thread,Event
import time

def task(e):
    print('客户端：可以连接了吗？，当前连接状态是%s'%e.is_set())
    e.wait()
    print('客户端：好啦，我连接成功')

def check(e):
    print('服务端：还不行，服务器设置了3秒等待时间')
    time.sleep(3)
    e.set()
    print('服务端：可以连接了,设置连接状态为%s'%e.is_set())

if __name__ == '__main__':
    e = Event()
    t1 = Thread(target = task,args = (e,))
    t2 = Thread(target = check,args = (e,))

    t1.start()
    t2.start()