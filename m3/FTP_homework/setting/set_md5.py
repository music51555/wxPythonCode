import hashlib
import os

def set_md5(msg):
    if os.name == 'nt':
        msg_bytes = msg.encode('GBK')
    else:
        msg_bytes = msg.encode('utf-8')
    m = hashlib.md5(msg_bytes)
    print(m.hexdigest())

set_md5('hello')