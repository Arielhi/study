#-*- coding:utf-8 -*-#-*- coding:utf-8 -*-
from robot.api import TestSuite
from robot.api import ResultWriter

if __name__ == '__main__':
    print("robot framework实例")

    # 创建套件
    suite = TestSuite("搜索测试套件")
    # 导入seleniumLibrary库
    suite.resource.imports.library("SeleniumLibrary")

    # 以下是测试步骤
    # 创建测试用例：启动浏览器
    test_01 = suite.tests.create("启动浏览器")
    test_01.keywords.create("Open Browser",
                            args=["http://www.baidu.com", "Chrome"])
    test_01.keywords.create("Title Should Be",
                            args=["百度一下，你就知道"])

    # 创建测试用例：搜索测试
    test_02 = suite.tests.create("关键字搜索测试")
    test_02.keywords.create("Input Text",
                            args=["id=kw","Python"])
    test_02.keywords.create("Click Button",
                            args=["id=su"])
    test_02.keywords.create("Sleep", args=["5s"])

    # 创建测试用例：断言验证搜索结果页标题
    test_03 = suite.tests.create("断言验证搜索结果页标题")
    test_03.keywords.create("Title should be",
                            args=["Python_百度搜索"])

    # 创建测试用例：关闭测试用例
    test_04 = suite.tests.create("关闭浏览器")
    test_04.keywords.create("Close All Browsers")


    # 运行套件
    result = suite.run(critical="百度搜索", output="output_py.xml")

    # 生成日志、报告文件
    ResultWriter(result).write_results(report="report_py.html",
                                       log="log_py.html")