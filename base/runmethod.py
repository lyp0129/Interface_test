# coding:utf-8


import requests
import json


class Runmethod:

    def post_main(self, url, data, header=None):

        if header is not None:
            # json=data是根据返回数据的格式去选择的

            res = requests.post(url=url, json=data, headers=header).json()
        else:
            res = requests.post(url=url, json=data).json()

        return json.dumps(res, ensure_ascii=False, indent=2)
        # return res.json()

    def get_main(self, url, data=None, header=None):

        if header is not None:
            res = requests.get(url=url, data=data, headers=header).json()

        else:
            res = requests.get(url=url, data=data).json()

        return json.dumps(res, indent=2)

    def run_main(self, method, url, data=None, header=None):

        if method == "post":
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)

        return res


if __name__ == '__main__':
    test = Runmethod()
    url = "https://couple-api.jizhangapp.com/user/birthday"

    url2 = "https://quanzi.qufaya.com/wxapp/join/app/code?token=cb92a909-cbf8-4fd1-b551-9347f460db51"

    appjoin = {"birthday": "818352000000", "calendar": "0"}

    headers = {"qz-token": "983c15ad-d9d1-493e-bc00-04c68f3f982d"}

    a = test.run_main("post", url, appjoin, headers)

    print(a)
