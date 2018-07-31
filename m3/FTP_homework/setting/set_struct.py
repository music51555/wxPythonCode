import struct
import json
import sys

def send_message(socket_obj,header_info):
    header_json = json.dumps(header_info)
    header_bytes = header_json.encode('utf-8')
    socket_obj.send(struct.pack('i', len(header_bytes)))
    socket_obj.send(header_bytes)
    return

def recv_message(socket_obj):
    while True:
        try:
            header = socket_obj.recv(4)
            break
        except BlockingIOError:
            print('循环了1')
            continue
    if not header:
        return
    header_size = struct.unpack('i', header)[0]
    while True:
        try:
            header_bytes = socket_obj.recv(header_size)
            break
        except BlockingIOError:
            print('循环了2')
            continue
    header_dict = json.loads(header_bytes.decode(sys.getdefaultencoding()))
    return header_dict
