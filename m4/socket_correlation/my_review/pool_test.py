import time,random
from concurrent.futures import ThreadPoolExecutor

def write_code(name):
    print('%s is writing code'%name)
    time.sleep(random.randint(1,3))
    code_line = random.randint(1,15)
    return {'name':name,'line':code_line}

def check_code(code_dict):
    print('%s write %s line code'%(code_dict['name'],code_dict['line']))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(2)
    code_dict = pool.submit(write_code,'alex').result()
    check_code(code_dict)
    code_dict = pool.submit(write_code, 'wxx').result()
    check_code(code_dict)
    code_dict = pool.submit(write_code, 'yh').result()
    check_code(code_dict)
