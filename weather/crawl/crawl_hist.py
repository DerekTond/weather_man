#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode


# ----------------------------------
# 历史上的今天调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/63
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = "*********************"

    # 1.事件列表
    request1(appkey, "GET")

    # 2.根据ID查询事件详情
    request2(appkey, "GET")


# 事件列表
def request1(appkey, m="GET"):
    url = "http://api.juheapi.com/japi/toh"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "v": "",  # 版本，当前：1.0
        "month": "",  # 月份，如：10
        "day": "",  # 日，如：1

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


# 根据ID查询事件详情
def request2(appkey, m="GET"):
    url = "http://api.juheapi.com/japi/tohdet"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "v": "",  # 版本，当前：1.0
        "id": "",  # 事件ID

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])

        else:
            print("%s:%s" % (res["error_code"], res["reason"]))

    else:
        print
        "request api error"


if __name__ == '__main__':
    main()