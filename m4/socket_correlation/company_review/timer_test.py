from threading import Thread,Timer
import random,string

class In_code(Thread):

    def make_code(self):
        code = ''.join(random.sample(string.ascii_lowercase + string.ascii_uppercase,4))
        return code

    def verify_code(self):
        self.code = self.make_code()
        t = Timer(interval=5, function=self.verify_code)
        t.start()

    def check(self):
        while True:
            print(self.code)
            msg = input('>>>:')
            if msg == self.code:
                print('验证成功')
                continue
            else:
                print('验证失败')
                continue

if __name__ == '__main__':
    i = In_code()

    i.verify_code()
    i.check()