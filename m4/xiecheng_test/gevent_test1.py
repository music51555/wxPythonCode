import gevent,time
from gevent import monkey;monkey.patch_all()

def eat(name):
    print('%s is eat1'%name)
    time.sleep(7)
    print('%s is eat2'%name)

def play(name):
    print('%s is play1'%name)
    gevent.sleep(4)
    print('%s is play2'%name)

def task(name):
    print('%s is task1'%name)
    gevent.sleep(1)
    print('%s is task2'%name)

if __name__ == '__main__':
    start_time = time.time()
    g1 = gevent.spawn(eat,'alex')
    g2 = gevent.spawn(play,'alex')
    g3 = gevent.spawn(task,'alex')

    g1.join()
    g2.join()
    g3.join()
    print('主')

    end_time = time.time()
    print(end_time - start_time)
