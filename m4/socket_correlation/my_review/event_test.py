# import time
# from threading import Thread,Event
#
# def client(name,event):
#     print('%s is connecting...'%name)
#     event.wait()
#     print('%s connect success!'%name)
#
# def server(name,event):
#     print('%s recv connect,wait please'%name)
#     time.sleep(3)
#     event.set()
#
# if __name__ == '__main__':
#     event = Event()
#     t1 = Thread(target=client,args=('客户端',event))
#     t2 = Thread(target=server,args=('服务端',event))
#     t1.start()
#     t2.start()

import time
from threading import Thread,Event
from multiprocessing import Process,Event

def client(name,event):
    n = 0

    while not event.is_set():
        if n == 3:
            print('%s is connect fail'%name)
            return
        print('%s is connecting'%name)
        time.sleep(1)
        n += 1

    event.wait()
    print('%s is connect success!'%name)

def server(name,event):
    time.sleep(0.2)
    print('%s recv connect'%name)
    time.sleep(2)
    event.set()

if __name__ == '__main__':
    event = Event()
    p1 = Process(target=client,args=('客户端',event))
    p2 = Process(target=server,args=('客户端',event))

    p1.start()
    p2.start()