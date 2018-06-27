import time

class Hello:

    def hello(self,name):
        d = time.localtime()
        r = list(range(0, 24))
        if d.tm_hour in r[:9]:
            return print('%s,早上好' % name)
        elif d.tm_hour in r[9:12]:
            return print('%s,上午好' % name)
        elif d.tm_hour in r[12:13]:
            return print('%s,中午好' % name)
        elif d.tm_hour in r[13:18]:
            return print('%s,下午好' % name)
        elif d.tm_hour in r[18:]:
            return print('%s,晚上好' % name)