import hashlib
import sys

def set_md5(msg):
    msg_bytes = msg.encode(sys.getdefaultencoding())
    m = hashlib.md5(msg_bytes)
    return m.hexdigest()

def set_file_md5(file):
    print(file)
    f = open(file,'rb')
    m = hashlib.md5()
    for line in f:
        m.update(line)
    f.close()
    return m.hexdigest()