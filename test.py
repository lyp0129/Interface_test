# coding:utf-8
import requests
import json


class Testjenkins:
    def getmain(self, url):
        res = requests.get(url=url, data=None).json()

        return res

    def postmain(self, url, data=None, json=None):
        res = requests.post(url=url, json=json).json()  # url, data=None, json=None, **kwargs

        return res

    def runmain(self, method, url, data=None, json=None):
        if method == "post":
            res = self.postmain(url, json)
        else:
            res = self.getmain(url)
        return res


if __name__ == '__main__':
    test = Testjenkins()
    url = "https://quanzi.jizhangapp.com/discovery/user/card"
    data = {"Authorization": "60c9fc6f-e0b1-4945-9c67-dfa991883fdf"}
    a = test.runmain("get", url)
    b = requests.get(url, headers=data).json()
    print(json.dumps(b, indent=2))
