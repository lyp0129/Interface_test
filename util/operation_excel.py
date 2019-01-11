# coding:utf-8
import xlrd
from xlutils.copy import copy

'''
操作测试用例的excel表
'''


class OperationExcel:

    def __init__(self, excel_path=None, sheet_id=None):  # sheet_id是excel中的第几张表的下标
        if excel_path:
            self.excel_path = excel_path
            self.sheet_id = sheet_id
        else:
            # self.excel_path = "/Users/lyp/Desktop/jiekou/loveing.xls"
            self.excel_path = "/Users/quanzi/Desktop/jiekou/love/loveing.xls"
            self.sheet_id = 0

    # 获取测试用例的excel表

    def get_data(self):
        # 获取excel
        data = xlrd.open_workbook(self.excel_path)
        # 获取excel中第几张工作表
        tables = data.sheet_by_index(self.sheet_id)

        return tables

    # 获取ecxel中的行数

    def get_lines(self):
        lines = self.get_data().nrows
        return lines

    # 获取单元格内容

    def get_content(self, row, col):  # row行，col列
        content = self.get_data().cell_value(row, col)
        return content

    # 写入数据

    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.excel_path)

    # 根据依赖的id找到在对应的id

    def rely_id_get_row_id(self):
        pass

    # 根据行id找到在第几行

    def according_id_get_row_num(self):
        pass

    # 根据行号获得内容

    def according_row_num_get_row_content(self):
        table = self.get_data()


if __name__ == '__main__':
    oda = OperationExcel()
    # print(oda.get_data().name)
    # print(oda.get_lines())
    print(oda.get_content(1, 2))
