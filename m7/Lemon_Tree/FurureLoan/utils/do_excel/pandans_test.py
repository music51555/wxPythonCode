import pandas
from utils.case_conf.case_conf import GetConf
from settings import CONF_INI
from settings import EXCEL_FILE
from openpyxl import load_workbook
import random

class DoExcel:
    api_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/'

    def __init__(self,file_name):
        self.file_name = file_name
        self.wb = load_workbook(self.file_name)

    def get_conf(self):
        conf_value = GetConf(CONF_INI,'CASE_MODE','case_mode').get_conf()
        return conf_value

    def read_init_tel(self):
        init_tel = int(pandas.read_excel(self.file_name,'init').ix[0,1])+1
        return init_tel

    def get_case_list(self):
        case_list = []
        mode_info = self.get_conf()
        init_tel = self.read_init_tel()
        print(init_tel)
        for sheet_name,case_mode in eval(mode_info).items():
            # index_col表示索引列，0为第一列
            self.df = pandas.read_excel(self.file_name,sheet_name)
            if case_mode == 'all':
                for row in self.df.index.values:
                    case_info = self.df.ix[row].to_dict()
                    if case_info['case_data'].find('$(tel)')!=-1:
                        case_info['case_data'] = case_info['case_data'].replace('$(tel)',str(init_tel))
                    case_info['url'] = self.api_url + sheet_name
                    case_info['sheet_name'] = sheet_name
                    case_list.append(case_info)
            elif case_mode == 'random':
                rand_int = random.choice([i for i in range(1,max(self.df.index.values)+2)])
                for case in self.df.sample(rand_int).values:
                    case_info = self.df.ix[case[0]-1].to_dict()
                    if case_info['case_data'].find('$(tel)')!=-1:
                        case_info['case_data'] = case_info['case_data'].replace('$(tel)',str(init_tel))
                    case_info['sheet_name'] = sheet_name
                    case_info['url'] = self.api_url + sheet_name
                    case_list.append(case_info)
            else:
                for row in case_mode:
                    case_info = self.df.ix[row-1].to_dict()
                    if case_info['case_data'].find('$(tel)')!=-1:
                        case_info['case_data'] = case_info['case_data'].replace('$(tel)',str(init_tel))
                    case_info['url'] = self.api_url + sheet_name
                    case_info['sheet_name'] = sheet_name
                    case_list.append(case_info)
        # 最后保存并关闭文件
        self.update_tel('init',init_tel)
        return case_list

    def update_tel(self,sheet_name,new_tel):
        sheet = self.wb[sheet_name]
        sheet.cell(2,2).value = new_tel+1
        self.wb.save(self.file_name)

    def update_success(self,sheet_name,is_sucess,case_info):
        sheet = self.wb[sheet_name]
        sheet.cell(case_info['case_id'] + 1, 6).value = is_sucess
        self.wb.save(self.file_name)

    def update_result(self,sheet_name,result,case_info):
        sheet = self.wb[sheet_name]
        sheet.cell(case_info['case_id'] + 1, 5).value = str(result)
        self.wb.save(self.file_name)

if __name__ == '__main__':
    DoExcel(EXCEL_FILE).get_case_list()

