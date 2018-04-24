#-*- coding:utf-8 -*-
"""
python解析html使用：HTMLParser
常用方法：
HTMLParser.feed(data)：接收字符串类型的html内容
*.close()：遇到文件结束标签后的处理方法
*.reset()：重置
*.getpos()：返回当前行和相应的偏移量
*.handle_starttag(tag,attrs)：对开始标签进行处理
*.handle_endtag(tag)：对结束标签进行处理
*.handle_data(data)：对标签间的数据进行处理
*.handle_comment(data)：对注释进行处理
"""
from html.parser import HTMLParser
import http.client


class BaiduHTMLParser(HTMLParser):
    data = []
    data_key = ""

    def __init__(self):
        HTMLParser.__init__(self)
        self.is_a = False

    def handle_starttag(self, tag, attrs):
        # 处理开始为a的标签
        if tag == "a":
            self.is_a = True
            for name, value in attrs:
                if name == "href":
                    # 提取href
                    self.data_key = value

    def handle_data(self, data):
        # 处理a标签间的数据
        if self.is_a and self.lasttag == 'a':
            # 将href属性作为key， 文本作为data构建字典
            self.data.append({self.data_key:data})

    def handle_endtag(self, tag):
        if self.is_a and self.lasttag == 'a':
            self.is_a = False

    def get_data(self):
        # 返回提取的信息
        return self.data

if __name__ == '__main__':
    print("python HTML解析")
    print("访问百度首页获取html源码")

    # 构建链接
    conn = http.client.HTTPSConnection("www.baidu.com")
    # 获取源码
    conn.request("GET", "/")
    r1 = conn.getresponse()
    data = r1.read().decode(encoding="utf-8")
    print(data)
    # 解析并提取
    sinaMailHTMLParser = BaiduHTMLParser()
    sinaMailHTMLParser.feed(data)   # 接收并解析
    links = sinaMailHTMLParser.get_data()
    print(links)