import struct
import json

def struct_pack(socket_obj,header_info):
    header_json = json.dumps(header_info)
    header_bytes = header_json.encode('GBK')
    socket_obj.send(struct.pack('i', len(header_bytes)))
    socket_obj.send(header_bytes)
    return

def struct_unpack(socket_obj):
    try:
        header = socket_obj.recv(4)
        # if not header:
        #     return
        header_size = struct.unpack('i', header)[0]
        header_bytes = socket_obj.recv(header_size)
        header_dict = json.loads(header_bytes.decode('GBK'))
        return header_dict
    except ConnectionResetError as e:
        print(e)
        return
