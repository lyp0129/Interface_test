# coding:utf-8
class CommonUtill:

    def is_contain(self, str_one, str_two):
        '''

        判断一个字符串是否在另一个字符串中
        '''
        if str_one in str_two:
            flog = True
        else:
            flog = False

        return flog


if __name__ == '__main__':
    a = CommonUtill()
    c = a.is_contain("hello", "helloo")
    print(c)
