import pandas
from utils.case_conf.case_conf import GetConf
from settings import CONF_INI
from settings import EXCEL_FILE
import random

class DoExcel:
    api_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/'

    def __init__(self,file_name):
        self.file_name = file_name

    def get_conf(self):
        conf_value = GetConf(CONF_INI,'CASE_MODE','case_mode').get_conf()
        return conf_value

    def get_case_list(self):
        case_list = []
        mode_info = self.get_conf()
        # 在准备打开每一个工作簿前，创建一个writer对象，来准备依次写入工作簿中的内容
        self.writer = pandas.ExcelWriter('test_case.xlsx')
        for sheet_name,case_mode in eval(mode_info).items():
            # index_col表示索引列，0为第一列
            self.df = pandas.read_excel(self.file_name,sheet_name,index_col=0)
            if case_mode == 'all':
                for row in self.df.index.values:
                    case_info = self.df.ix[row].to_dict()
                    print(case_info)
                    case_info['url'] = self.api_url + sheet_name
                    case_info['sheet_name'] = sheet_name
                    self.update_phone(case_info,row)
                    case_list.append(case_info)
            elif case_mode == 'random':
                rand_int = random.choice([i for i in range(1,max(self.df.index.values)+2)])
                for case in self.df.sample(rand_int).values:
                    case_info = self.df.ix[case[0]-1].to_dict()
                    case_info['sheet_name'] = sheet_name
                    case_info['url'] = self.api_url + sheet_name
                    self.update_phone(case_info,case_info['case_id'])
                    case_list.append(case_info)
            else:
                for row in case_mode:
                    case_info = self.df.ix[row-1].to_dict()
                    case_info['url'] = self.api_url + sheet_name
                    case_info['sheet_name'] = sheet_name
                    self.update_phone(case_info,row)
                    case_list.append(case_info)
        # 最后保存并关闭文件
        self.writer.save()
        self.writer.close()
        return case_list

    def update_phone(self,case_info,row):
        case_data = case_info['case_data']
        # 读取出的case_data为字符串，将其转换为字典类型，用于盘点mobilephone的key是否有值
        case_data = eval(case_data)
        if case_data['mobilephone']:
            # 准备写入会excel前，将字典还原会字符串类型
            case_data['mobilephone'] = str(int(case_data['mobilephone']) + 1)
            # df不支持df[i][j]赋值，只能使用df.loc(切片，列名)方法进行赋值
            self.df.loc[row:row,['case_data']] = str(case_data)
            # 通过loc方法设置值后，将其在已经打开writer对象中对应工作簿中写入内容
            self.df.to_excel(self.writer,case_info['sheet_name'])

if __name__ == '__main__':
    DoExcel(EXCEL_FILE).get_case_list()

