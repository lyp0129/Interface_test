# coding:utf-8
from util.operation_excel import OperationExcel
from data.data_config import global_var
from util.operation_json import OperationJson
import json


class Getdata:

    def __init__(self):
        self.opera_excel = OperationExcel()
        self.get_data = global_var()

    # 获取Excel行数
    def get_line(self):
        return self.opera_excel.get_lines()

    # 是否运行
    def is_run(self, row):
        col = self.get_data.run
        run_model = self.opera_excel.get_content(row, int(col))

        if run_model == "yes":
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = self.get_data.header
        header = self.opera_excel.get_content(row, int(col))
        headers = json.dumps(header)
        if header == "":
            return None
        else:
            return headers

    # 获取请求方式
    def run_way(self, row):
        col = self.get_data.request_way
        request_method = self.opera_excel.get_content(row, int(col))
        return request_method

    # 获取url

    def get_url(self, row):
        col = self.get_data.url
        request_url = self.opera_excel.get_content(row, int(col))
        return request_url

    # 获取请求数据

    def get_request_data(self, row):
        col = self.get_data.data
        request_data = self.opera_excel.get_content(row, int(col))
        if request_data == "":
            return None
        else:
            return request_data

    # 读取json文件中的数据
    def get_data_for_json(self, row):
        # Opera_json = OperationJson('/Users/lyp/Desktop/jiekou/lover.json')
        Opera_json = OperationJson("/Users/quanzi/Desktop/jiekou/love/lover.json")
        request_data_r = Opera_json.get_json_data(self.get_request_data(row))
        if request_data_r == '':
            return None
        else:
            return request_data_r

    # 读取预期数据
    def get_data_for_expect(self, row):
        col = self.get_data.expect
        expect_data = self.opera_excel.get_content(row, int(col))
        if expect_data == '':
            return None
        else:
            return expect_data

    # 读取实际结果

    def get_failed_results(self, row):
        col = self.get_data.result
        failed_result = self.opera_excel.get_content(row, int(col))
        if failed_result == '':
            return None
        else:
            return failed_result

    # 读取case_tile结果

    def get_case_Title(self, row):
        col = self.get_data.request_name

        case_Title = self.opera_excel.get_content(row, int(col))

        if case_Title == '':
            return None
        else:
            return case_Title

    def write_result(self, row, value):
        col = self.get_data.get_result()
        self.opera_excel.write_value(row, int(col), value)


if __name__ == '__main__':
    test = Getdata()
    # print(test.is_run(2))

    # print(test.is_run(1))
    # print(test.is_header(2))
    # print(test.run_way(1))
    # print(test.get_url(2))
    # print(test.get_request_data(1))
    a = test.is_header(2)
    c = json.dumps(a)
    d = test.get_case_Title(1)
    print(d)
