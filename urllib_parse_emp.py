#-*- coding:utf-8 -*-

import urllib.request
from urllib.parse import urlparse

if __name__ == '__main__':
    '''
    parse模块可将url拆分或组合
    '''
    print("urllib url切割实例")
    url = "http://username:password@www.baidu.com:80/q=python"

    result = urlparse(url)
    print("切割后的整体结果：")
    print(result)
    print("协议：", result.scheme)
    print("连接字符串：", result.netloc)
    print("端口号：", result.port)
    print("uri资源：", result.path)
    print("用户名：", result.username)
    print("密码：", result.password)

    '''
    request模块，核心模块。
    定义函数、类来实现http/https相关功能
    '''
    print("读取www,pyhto.org首页的HTML源码")
    response = urllib.request.urlopen("http://www.python.org")
    print("结果：")
    print(response.read())
