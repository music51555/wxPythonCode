import gevent,time
from gevent import monkey;monkey.patch_all()

def eat(name):
    print('%s is eat1'%name)
    time.sleep(2)
    print('%s is eat2'%name)

def play(name):
    print('%s is play1'%name)
    time.sleep(3)
    print('%s is play2'%name)

if __name__ == '__main__':
    g1 = gevent.spawn(eat,'alex')
    g2 = gevent.spawn(play,'alex')

    gevent.joinall([g1,g2])