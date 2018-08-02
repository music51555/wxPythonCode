from prettytable import PrettyTable

def set_table(total_list):
    x = PrettyTable(['序号', '文件名称', '文件大小', '文件格式', '上传日期'])
    for line in total_list:
        x.add_row(line)
    x.align['序号'] = 'm'
    x.align['文件名称'] = 'l'
    x.align['文件大小'] = 'l'
    x.align['文件格式'] = 'm'
    x.align['上传日期'] = 'l'
    print(x)

