#-*- coding:utf-8 -*-
import yaml

if __name__ == '__main__':
    print("python yaml示例")
    document = """
    种类：植物
    基本信息：
        名称：栗
        学名：Castanea mollissima
    """

    # 将yaml格式转换成dict类型
    load = yaml.load(document)
    print(type(load))
    print(load)
    print("---"*30)
    #将python对象转换成yaml
    output = yaml.dump(load)
    print(type(output))
    print(output)
