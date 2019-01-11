# -*- coding: utf-8 -*-
# coding=utf-8
"""
日报
"""
# import reload
import smtplib
import os
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from data.get_data import Getdata
import sys


# reload(sys)

# sys.setdefaultencoding('utf-8')


class MyEmail:

    def __init__(self):
        # 发件人
        self.user = None

        # 发件人密码
        self.passwd = None

        # 字符串列表，邮件发送地址
        self.to_list = []

        # 字符串列表，抄送邮件发送地址
        self.cc_list = []

        # 邮件主题
        self.tag = None

        # 邮件内容
        self.content = None

        # 邮件附件
        self.doc = None

        self.get_data = Getdata()

    def send(self):
        """
        发送邮件
        """
        try:
            # 邮件服务器及端口号，SMTP_SSL默认使用465端口号，端口号可省略
            server = smtplib.SMTP_SSL("smtp.exmail.qq.com", port=465)
            # server = smtplib.SMTP_SSL("imap.exmail.qq.com", port=465)
            # 发送者的用户，密码
            server.login(self.user, self.passwd)

            # 发送的邮件地址("from_addr:邮件发送者地址"，"to_addrs:字符串列表，邮件发送地址"，"msg:发送消息")
            server.sendmail("<%s>" % self.user, self.to_list, self.get_attach())

            server.close()

            print("send email successful")
        except Exception as e:
            logging.exception(e)
            print("send email failed %s" % e)

    def get_attach(self):
        """
        构造邮件内容
        """
        attach = MIMEMultipart()
        if self.tag is not None:
            # 主题,最上面的一行
            attach["Subject"] = self.tag

        if self.user is not None:
            # 显示在发件人
            # attach["From"] = "发件人姓名，可以自定义<%s>" % self.user
            attach["From"] = "大鹏<%s>" % self.user

        if self.to_list:
            # 收件人列表
            attach["To"] = ";".join(self.to_list)

        if self.cc_list:
            # 抄送列表
            attach["Cc"] = ";".join(self.cc_list)

        if self.content:
            # 邮件的内容
            c = MIMEText(self.content, _subtype='plain', _charset='utf-8')
            attach.attach(c)

        if self.doc:
            # 估计任何文件都可以用base64，比如rar等
            # 文件名汉字用gbk编码代替
            name = str(os.path.basename(self.doc).encode("gbk"))
            f = open(self.doc, "rb")
            doc = MIMEText(f.read(), "base64", "gb2312")
            doc["Content-Type"] = 'application/octet-stream'
            doc["Content-Disposition"] = 'attachment; filename="' + name + '"'
            attach.attach(doc)
            f.close()

        return attach.as_string()

    # 根据全部的实际结果
    def Get_results_value_all(self):
        data = self.get_data
        line = data.get_line()
        results_value_all = []
        for i in range(1, line):
            results = data.get_failed_results(i)
            results_value_all.append(results)
        return results_value_all

    # 根据全部的实际结果获取失败的value
    def Get_results_fail_value(self):
        fail_value = []
        results_fail = self.Get_results_value_all()

        # print(results_fail)
        for i in range(len(results_fail)):

            if results_fail[i] != "pass":
                fail_value.append(str(results_fail[i]))
        # print(fail_value)

        return fail_value

    # 根据全部的实际结果获取id

    def Get_results_fail_id(self):
        fail_value_id = []
        results_fail = self.Get_results_value_all()
        # print(results_fail)
        for i in range(len(results_fail)):
            if results_fail[i] != "pass":
                fail_value_id.append(str(i))
                # print(i)

        return fail_value_id

    def test(self):
        results_fail = self.Get_results_value_all()
        # print(results_fail)
        for i, value in enumerate(results_fail):

            print(i, value)
            if value != "pass":
                print(value)

    # 根据失败的case id 获取title

    def Get_case_Title(self):
        fail_title = []
        data = self.get_data
        fail_id = self.Get_results_fail_id()
        # print(fail_id)
        for i in fail_id:
            title = data.get_case_Title(int(i))
            fail_title.append(title)

        return fail_title

    def xx(self):
        fail_id = self.Get_results_fail_id()
        fail_value = self.Get_results_fail_value()
        fail_title = self.Get_case_Title()
        ls3 = ",".join(fail_id)
        ls4 = ",".join(fail_title)
        ls5 = ",".join(fail_value)
        print(ls3)
        print(ls4)
        print(ls5)
        print(type(ls3))
        print(type(ls4))
        print(type(ls5))

    def test_result(self, pass_list, fail_list):
        # my = MyEmail()
        fail_id = self.Get_results_fail_id()
        fail_value = self.Get_results_fail_value()
        fail_title = self.Get_case_Title()
        ls3 = ",".join(fail_id)
        ls4 = "".join(fail_title)
        ls5 = ",".join(fail_value)

        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)
        # 需要添加密码和账号
        self.user = "xxx.com"
        self.passwd = "xxxx"
        self.to_list = ["dapeng@qufaya.com", ]
        # my.cc_list = ["292596031@qq.com", ]
        self.tag = "接口测试报告"
        self.doc = "/Users/quanzi/Desktop/jiekou/love/loveing.xls"
        # self.doc = "/Users/lyp/Desktop/jiekou/loveing.xls"
        self.content = "此次一共运行接口个数为:%s个，通过个数为:%s个，失败个数为:%s,通过率为:%s,失败率为:%s \n\n失败case id为：%s\n\n失败case 内容为：%s" % (
            count_num, pass_num, fail_num, pass_result, fail_result, ls3, ls5)
        self.send()


if __name__ == "__main__":
    my = MyEmail()
    my.user = "dapeng@qufaya.com"
    my.passwd = "DP1995zz"
    my.to_list = ["dapeng@qufaya.com"]
    # my.cc_list = ["292596031@qq.com", ]
    my.tag = "日报"
    a = my.doc = "/Users/lyp/Desktop/jiekou/loveing.xls"
    my.content = "zxc123"
    my.xx()

    # my.send()
    # my.test_result([1, 2, 3, 4, 5], [2, 3, 4, 7])
    # my.Get_case_Title()
