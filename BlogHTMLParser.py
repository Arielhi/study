#-*- coding:utf-8 -*-
"""
基本爬虫实例
爬去链接
"""
import urllib.parse
import urllib.request

from html.parser import HTMLParser

class BlogHTMLPaser(HTMLParser):
    data = []
    data_key = ""

    def __init__(self):
        HTMLParser.__init__(self)
        self.is_a = False

    def handle_starttag(self, tag, attrs):
        # 处理a标签
        if tag == "a":
            self.is_a = True
            for name,value in attrs:
                if name == "href":
                    self.data_key = value

    def handle_data(self, data):
        if self.is_a and self.lasttag=="a":
            # 将a标签的href属性值作为key，a的文本作为data构建字典
            self.data.append({self.data_key : data})

    def handle_endtag(self, tag):
        if self.is_a and self.lasttag=="a":
            self.is_a = False

    def get_data(self):
        # 返回所有提取到的数据
        return self.data

if __name__ == '__main__':
    print("urllib爬取博客园首页链接实例")

    url = "https://www.cnblogs.com/"
    # 访问首页
    response = urllib.request.urlopen(url)
    data = response.read().decode(encoding="utf-8")
    # 提取所有链接
    blogHtmlParser = BlogHTMLPaser()
    blogHtmlParser.feed(data)
    links = blogHtmlParser.get_data()
    print(links)