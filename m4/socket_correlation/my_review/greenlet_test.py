# from greenlet import greenlet
#
# def eat(name):
#     print('%s is eating'%name)
#     g2.switch('alex')
#     print('%s is eating to 2'%name)
#     g2.switch('alex')
#
# def play(name):
#     print('%s is playing'%name)
#     g1.switch('alex')
#     print('%s is playing to 2'%name)
#     g1.switch('alex')
#
# if __name__ == '__main__':
#     g1 = greenlet(eat)
#     g2 = greenlet(play)
#
#     g1.switch('alex')

import gevent,time
from gevent import monkey;monkey.patch_all()

def eat(name):
    print('%s is eating1'%name)
    time.sleep(3)
    print('%s is eating2'%name)

def play(name):
    print('%s is playing1'%name)
    time.sleep(5)
    print('%s is playing2'%name)

def see(name):
    print('%s is seeing1'%name)
    time.sleep(1)
    print('%s is seeing2'%name)

if __name__ == '__main__':
    g1 = gevent.spawn(eat,'alex')
    g2 = gevent.spawn(play,'alex')
    g3 = gevent.spawn(see,'alex')

    g1.join()
    g2.join()
    g3.join()