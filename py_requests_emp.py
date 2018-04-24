#-*- coding:utf-8 -*-
"""
requests功能：
Keep-Alive & 连接池
国际化域名和URL
带持久化Cookie的会话
浏览器式的SSL认证
内容自动解码
basic/Digest认证
key/value Cookie管理
自动解压
Unicode响应
HTTP/HTTPS代理支持
文件分块上传
流下载
连接超时
分块请求
支持.netrc
"""

import requests

if __name__ == '__main__':
    print("requests基本示例")

    # 发送HTTP GET请求，获取GitHub API列表
    r = requests.get("https://api.github.com")

    # 请求状态码
    status_code = r.status_code
    # 完整返回头
    headers = r.headers
    # 返回头的content-type值
    content_type = r.headers["content-type"]
    # 编码类型
    code = r.encoding
    # 返回的文本内容
    text = r.text
    # 返回的json格式的内容
    json_data = r.json()

    # 打印
    print("状态码：", status_code)
    print("返回头：", headers)
    print("content-type：", content_type)
    print("编码：", code)
    print("文本内容：", text)
    print("json串内容：", json_data)

    # 自定义请求头
    print("-----自定义请求头-----")
    url = "http://www.baidu.com"
    headers={
        "user-agent":"www.testingunion.com",
        "custom-head":"DeepTest"
    }
    # 发送带自定义头的请求
    r =  requests.get(url, headers=headers)

    print("-----requests post示例-----")
    url = "http://httpbin.org/post"
    headers = {"custom-header": "mypost"}
    # 要post的数据
    data = {
        "data_1":"deeptest",
        "data_2":"testingunion.com"
    }
    # 发送post请求
    r = requests.post(url,data=data,headers=headers)
    print(r.text)

    print("-----requests post json示例-----")
    url = "http://jsonplaceholder.typicode.com/posts"
    headers = {
        "custom-post":"my-post",
        "custom-header":"my-json-header"
    }
    # 要post的数据
    json_data = {
        "title":"deeptest",
        "body":"测试数据",
        "userId":"10"
    }
    # post json数据
    r = requests.post(url,json=json_data,headers=headers)
    print(r.text)


