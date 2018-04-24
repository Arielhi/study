*** Setting ***
# 使用SeleniumLibrary库实现搜索测试
Library    SeleniumLibrary

*** Variables ***
# 变量定义
${baidu}    http://www.baidu.com    # 首页
${browser}    Chrome    # 浏览器
${searchWord}    Python    # 搜索词
${search_input}    id=kw    # 搜索框id
${search_btn}    id=su    # 按钮

*** Test Cases ***
# 测试用例
启动浏览器
    Open Browsers

搜索测试
    Input Search Word
    Click Search Button

断言验证搜索结果：标题
    Assert Search Result

关闭浏览器
    Quit Search

*** Keywords ***
# 自定义关键字
Open Browsers
    Open Browser    ${baidu}    ${browser}
    Title Should Be    百度一下，你就知道

Input Search Word
    Input Text    ${search_input}    ${searchWord}
    Sleep    5s

Click Search Button
    Click Button    ${search_btn}
    Sleep    5s

Assert Search Result
    Title Should Be    Python_百度搜索

Quit Search
    Close All Browsers