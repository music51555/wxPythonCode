from threading import Thread,Event
import time

def conn(name,e):
    count = 0
    while not e.is_set():
        if count == 3:
            print('连接服务端失败')
            return
        print('%s is trying connect server,%s times'%(name,count))
        time.sleep(1)
        count += 1
    e.wait()
    print('连接服务端成功')

def check(e):
    print('正在连接服务端...')
    time.sleep(2)
    print('服务端准备就绪，可以申请连接')
    e.set()

if __name__ == '__main__':
    e = Event()
    t1 = Thread(target = conn,args = ('客户端',e))
    t2 = Thread(target = check,args = (e,))

    t1.start()
    t2.start()
