from greenlet import greenlet

def eat(name):
    print('%s is eat1'%name)
    g2.switch('alex')
    print('%s is eat2'%name)
    g2.switch('alex')

def play(name):
    print('%s is play1'%name)
    g1.switch('alex')
    print('%s is play2'%name)

if __name__ == '__main__':
    g1 = greenlet(eat)
    g2 = greenlet(play)

    g1.switch('alex')