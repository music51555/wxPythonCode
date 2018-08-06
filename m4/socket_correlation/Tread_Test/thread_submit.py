from concurrent.futures import ThreadPoolExecutor
import time,random

def write_code(name):
    print('%s is writing code'%name)
    time.sleep(random.randint(1,5))
    res = random.randint(5,10)
    return {'name':name,'line':res}

def check_code(code_obj):
    code_dict = code_obj.result()
    print('%s was write %s code'%(code_dict['name'],code_dict['line']))

if __name__ == '__main__':
    t = ThreadPoolExecutor(7)
    for i in range(10):
        #当通过t.submi()方法得到返回值后，
        print(t.submit(write_code,'alex%s'%i))
        t.submit(write_code,'alex%s'%i).add_done_callback(check_code)