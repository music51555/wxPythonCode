import configparser

conf = configparser.ConfigParser()
conf.read('conf.ini',encoding='utf-8')

res = conf.get('INFO','name')
print(res)

res = conf['SCHOOL']['class']
print(res)

print(conf.sections())
# 打印所有的section名称['INFO', 'SCHOOL', 'LEMON']

print(conf.options('INFO'))
# 通过section得到section下的option['name', 'age']

print(conf.items('INFO'))
# 通过items得到sections下的key-value键值对[('name', 'alex'), ('age', '30')]