#-*- coding:utf-8 -*-
"""
python解析xml：
1、SAX解析器（simple API for XML）
2、DOM（Document Object Model），解析成树，操作树
3、ElementTree，一个轻量级DOM
"""
import xml.etree.ElementTree as ET
import codecs
if __name__ == '__main__':
    print("python xml解析实例")

    '''
    载入xml有2种方式：
    1、从文件载入：返回xml数
    2、字符串载入：返回root元素对象
    '''

    # 从文件载入
    #tree = ET.parse('xml_data.xml')
    #获取根节点
    #root = tree.getroot()

    # 从xml字符串载入
    data = """
    <data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country></data>
    """
    root = ET.fromstring(data)
    # 打印根节点tag
    print(root.tag)
    # 遍历所有子节点及其属性
    print("---"*10)
    for child in root:
        print(child.tag, " ", child.attrib)

    # 提取year节点
    print("---" * 10)
    for child in root.iter("year"):
        print(child.tag, " ", child.text)
    # 修改，把节点所有的2011修改为2018
    print("---" * 10)
    for child in root.iter("year"):
        if child.text == "2011":
            child.text = "2018"
            child.set('updated', 'yes')
    print("修改2011->2017后")
    for child in root.iter("year"):
        print(child.tag, " ", child.text)

    # 新增节点，在country节点前加一个<wx>新节点</wx>
    print("---" * 10)
    for child in root.iter("country"):
        wx = ET.SubElement(child,"wx")
        wx.text = "新节点"
    # 遍历wx
    for child in root.iter("wx"):
        print(child.tag, " ", child.text)

    # 删除neighbor节点
    print("---" * 10)
    for child in root.findall("neighbor"):
        root.remove(child)

    # 保存上述操作
    xml_update_data = ET.tostring(root, encoding="unicode")
    # 写入文件xml_write_data.xml
    fp = codecs.open("xml_write_data.xml", "w", "utf-8")
    fp.write(xml_update_data)
    fp.close()
