#-*- coding:utf-8 -*-

from robot.api import TestSuite
from robot.api import ResultWriter
from robot.model import Keyword

"""
搜索测试封装
"""
class BaiduSerachTest:
    def __init__(self, name, librarys=["SeleniumLibrary"]):
        # 创建测试套件
        self.suit = TestSuite(name)
        # 导入支持库
        for lib in librarys:
            self.suit.resource.imports.library(lib)

    # 创建变量
    def create_variables(self):
        variables = {
            "${baidu}" : "http://www.baidu.com",
            "${browser}" : "Chrome",
            "${searchWord}" : "Python",
            "${search_input}" : "id=kw",
            "${search_btn}" : "id=su"
        }
        for k, v in variables.items():
            self.suit.resource.variables.create(k, v)

    # 创建测试用例：启动浏览器
    def open_browsers(self):
        test_01 = self.suit.tests.create("启动浏览器")
        test_01.keywords.create("Open Browser",
                                args=["${baidu}", "${browser}"])
        test_01.keywords.create("Title Should Be",
                                args=["百度一下，你就知道"])

    # 创建测试用例：搜索测试
    def search_word(self):
        test_02 = self.suit.tests.create("关键字搜索测试")
        test_02.keywords.create("Input Text",
                                args=["${search_input}", "${searchWord}"])
        test_02.keywords.create("Click Button",
                                args=["${search_btn}"])
        test_02.keywords.create("Sleep", args=["5s"])

    # 创建测试用例：断言
    def assert_title(self):
        test_03 = self.suit.tests.create("断言验证搜索结果页标题")
        test_03.keywords.create("Title should be",
                                args=["Python_百度搜索"])

    # 创建测试用例：关闭
    def close_browsers(self):
        test_04 = self.suit.tests.create("关闭浏览器")
        test_04.keywords.create("Close All Browsers")

    # 运行
    def run(self):
        self.create_variables()
        self.open_browsers()
        self.search_word()
        self.assert_title()
        self.close_browsers()
        # 运行套件
        result = self.suit.run(critical="百度搜索", output="output3.xml")
        ResultWriter(result).write_results(
            report="report3.html", log="log3.html"
        )

if __name__ == '__main__':
    print("Robot Framework示例-封装版")
    suite = BaiduSerachTest("搜索测试套件")
    suite.run()