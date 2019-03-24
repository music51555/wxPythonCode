from openpyxl import load_workbook

def get_value():
    wb = load_workbook('util/testcase_data.xlsx')
    login_sheet = wb['login']
    testcase_list = []
    for row in range(1,login_sheet.max_row+1):
        testcase = {}

        testcase['method_name'] = login_sheet.cell(row,1).value
        testcase['data'] = login_sheet.cell(row,2).value
        testcase['expect'] = login_sheet.cell(row,3).value

        testcase_list.append(testcase)

    return testcase_list
