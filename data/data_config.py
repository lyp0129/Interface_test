# coding:utf-8

'''
测试用例的excel表中每一项列
'''


class global_var:
    Id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'

    # case_id
    def get_id(self):
        return self.Id

    # request_name
    def get_request_name(self):
        return self.request_name

    # url
    def get_url(self):
        return self.url

    # 是否执行
    def get_run(self):
        return self.run

    # 请求方式
    def get_request_way(self):
        return self.request_way

    # header
    def get_header(self):
        return self.header

    # 数据依赖id
    def get_case_depend(self):
        return self.case_depend

    # 依赖的数据
    def get_data_depend(self):
        return self.data_depend

    #
    def get_field_depend(self):
        return self.field_depend

    # 请求数据
    def get_data(self):
        return self.data

    # 预期结果
    def get_expect(self):
        return self.expect

    # 实际结果
    def get_result(self):
        return self.result

    # 获取header的值
    def get_header_value(self):
        header = {
            "header": "123",
            "cookies": "lyp"
        }
        return self.get_header()
