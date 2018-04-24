#-*- coding:utf-8 -*-
import urllib.parse
import urllib.request

if __name__ == '__main__':
    print("urllib API实例说明")

    # 访问百度首页
    response = urllib.request.urlopen("http://www.baidu.com")
    # 打印首页HTML源码，获取完整响应内容
    html = response.read()
    print(html)

    # 打印header信息，提取header值用于下一个请求
    header = response.info()
    print(header)

    # 获取状态码，status code，可断言状态码
    status_code = response.getcode()
    print(status_code)

    # 打印本次请求的url
    url = response.geturl()
    print(url)