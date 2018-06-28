import struct

#i表示格式，表示integer整形，将准备send的数据长度转换为固定长度的bytes类型
res = struct.pack('i',123411)
print(res,type(res),len(res))

#解压包，获取到struct对象
obj = struct.unpack('i',res)
print(obj[0])