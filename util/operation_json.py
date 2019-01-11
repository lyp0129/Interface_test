# coding:utf-8
import json

'''
获取json表中请求数据的内存
'''


class OperationJson:

    def __init__(self, file_path=None):
        if file_path == None:
            # self.file_path = '/Users/lyp/Desktop/jiekou/4.0.1/she.json'
            self.file_path = "/Users/quanzi/Desktop/jiekou/love/lover.json"
        else:
            self.file_path = file_path
        # self.data = self.read_data()

    # 读取json文件
    def get_json(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    # 根据关键字过获取数据

    def get_json_data(self, leixing):

        data = self.get_json()
        if leixing == None:
            return None
        else:
            return data[leixing]
        # return data[leixing]


if __name__ == '__main__':
    opjson = OperationJson()
    # data_json.get_json()
    print(opjson.get_json_data('login'))
