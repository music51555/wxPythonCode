from openpyxl import load_workbook

class DoExcel:
    def __init__(self,file_name,sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.sheet = load_workbook(self.file_name)[self.sheet_name]

    def get_case_list(self):
        case_list = []
        for row in range(2,self.sheet.max_row+1):
            case_data = {}
            case_data['case_name'] = self.sheet.cell(row,3).value
            case_data['case_data'] = self.sheet.cell(row,4).value
            case_data['case_expected'] = self.sheet.cell(row,5).value
            case_list.append(case_data)

        return case_list