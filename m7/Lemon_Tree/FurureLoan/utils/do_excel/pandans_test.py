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
        for sheet_name,case_mode in eval(mode_info).items():
            print(case_mode)
            print(type(case_mode))
            df = pandas.read_excel(self.file_name,sheet_name)
            if case_mode == 'all':
                for row in df.index.values:
                    case_info = df.ix[row].to_dict()
                    case_info['url'] = self.api_url+sheet_name
                    case_list.append(case_info)
            elif case_mode == 'random':
                print('df.index.values',df.index.values)
                rand_int = random.choice([i for i in range(1,max(df.index.values)+2)])
                print(rand_int)
                for case in df.sample(rand_int).values:
                    case_info = df.ix[case[0]-1].to_dict()
                    case_info['url'] = self.api_url + sheet_name
                    case_list.append(case_info)
            else:
                for row in case_mode:
                    case_info = df.ix[row-1].to_dict()
                    case_info['url'] = self.api_url + sheet_name
                    case_list.append(case_info)
        return case_list

if __name__ == '__main__':
    DoExcel(EXCEL_FILE).get_case_list()

