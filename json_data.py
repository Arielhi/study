#-*- coding:utf-8 -*-
"""
json.dumps: python对象→json字符串
json.loads: json字符串→python对象

类型转换表
Python          json
dict            object
list,tuple      array
str,unicode     string
int,long,float  number
True            true
False           false
None            null
"""
import json

if __name__ == '__main__':
    print("python json标准库解析实例")

    # emp1: python对象转json对象
    data = [{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}]
    json_data = json.dumps(data)
    print("转化前")
    print(type(data))
    print(data)
    print("-"*60)
    print("转化后")
    print(type(json_data))
    print(json_data)

    # emp2: json对象转python对象
    print()
    print("json对象转python对象")
    python_data = json.loads(json_data)
    print(type(python_data))
    print(python_data)

    # emp3: 转为json对象后格式化输出
    print()
    print("转为json对象后格式化输出实例")
    json_data2 = json.dumps(data, sort_keys=True, indent=4, separators=(",", ":"))
    print(json_data2)

    # emp4: 从文件加载json转化为python对象
    print()
    print("从文件加载json转化为python对象实例")
    fp = open("json_data.json", "r")
    json_data3 = json.load(fp)
    #print(type(fp))
    print(type(json_data3))
    print(json_data3)
    fp.close()

    # emp5: 将json字符串对象存入文件
    print()
    print("将json字符串对象存入文件")
    data_w = [{'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}]
    fp = open("json_write.json", "w")
    # 可读式写入
    json.dump(data_w, fp, sort_keys=True, indent=4, separators=(",", ":"))
    fp.close()