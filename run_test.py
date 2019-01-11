# coding:utf-8
from base.runmethod import Runmethod
from data.get_data import Getdata
from util.CommonUtill import CommonUtill
from util.send_email import MyEmail


class Runtest:

    def __init__(self):
        self.run_method = Runmethod()
        self.get_data = Getdata()
        self.com_until = CommonUtill()
        self.send_email = MyEmail()

    def gorun(self):
        pass_count = []
        fail_count = []
        headers = {"qz-token": "a95bad3f-5330-4acc-aa6c-d3e5cc04b22d"}
        line = self.get_data.get_line()
        for i in range(1, line):
            is_run = self.get_data.is_run(i)
            if is_run:
                url = self.get_data.get_url(i)

                run_way = self.get_data.run_way(i)
                data = self.get_data.get_data_for_json(i)
                # header = self.get_data.is_header(i)
                expect = self.get_data.get_data_for_expect(i)
                res = self.run_method.run_main(run_way, url, data, headers)
                if self.com_until.is_contain(expect, res):
                    print("pass")
                    self.get_data.write_result(i, "pass")
                    pass_count.append(i)
                else:
                    print("fail")
                    self.get_data.write_result(i, res)
                    fail_count.append(i)

        self.send_email.test_result(pass_count,fail_count)


if __name__ == '__main__':
    test = Runtest()
    a = test.gorun()
    # print(a)
