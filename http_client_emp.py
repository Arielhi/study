#-*- coding:utf-8 -*-
import http.client, urllib.parse

if __name__ == '__main__':
    print("http.client示例")
    print("GET方法示例")

    # 初始化
    conn = http.client.HTTPSConnection("www.python.org")
    # 发送GET请求
    conn.request("get", "/")
    # 获取响应
    r1 = conn.getresponse()
    # 打印状态码、 对应说明、协议版本
    print(r1.status, r1.reason, r1.version)
    # 读取响应内容
    data1 = r1.read()

    # 分chunck读取内容
    conn.request("GET", "/")
    r1 = conn.getresponse()
    while not r1.closed:
        # 每次读取200bytes
        r1_data = r1.read(200)
        if len(r1_data) == 0:
            break
        print(r1_data)

    # 请求不存在的url
    conn.request("GET", "/parrot.spam")
    r2 = conn.getresponse()
    print(r2.status, r2.reason)
    data2 = r2.read()
    # 断开连接
    conn.close()

    print("http.client HEAD方法")
    conn = http.client.HTTPSConnection("www.python.org")
    conn.request("HEAD", "/")
    res = conn.getresponse()
    print(res.status, res.reason)

    data = res.read()
    print(len(data))
    conn.close()

    print("http.client POST方法")
    params = urllib.parse.urlencode({'@number':19999,
                                     '@type':'issue',
                                     '@action':'show'})
    # http头参数
    headers = {"Content-type":
               "application/x-www-form-urlencoded",
               "Accept":'show'}
    conn = http.client.HTTPConnection("bugs.python.org")
    # 把请求头和参数一起传入
    conn.request("POST","",params,headers)
    # 获取响应对象
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data)
    conn.close()