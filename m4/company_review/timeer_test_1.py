from threading import Timer,current_thread
import string,random

class In_Code():
    def make_code(self):
        self.code = ''.join(random.sample(string.ascii_lowercase + string.ascii_uppercase ,4))

        t = Timer(interval = 5,function = self.make_code)
        t.start()

    def check_code(self):
        while True:
            print(self.code)
            msg = input('请输入验证码：')
            if msg == self.code:
                print('验证成功')
                continue
            else:
                print('验证失败')
                continue

if __name__ == '__main__':
    i = In_Code()
    i.make_code()
    i.check_code()