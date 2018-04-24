#-*- coding:utf-8 -*-
import csv

if __name__ == '__main__':
    print("python csv 文件读写操作")

    # 写入CSV文件
    print("写入一些简单的数据到csv_data.csv文件")
    with open("csv_data.csv", "w", newline="") as csvfile:
        spamwriter = csv.writer(csvfile,delimiter=",")
        spamwriter.writerow(["草莓"]*5 + ["蛋糕"])
        spamwriter.writerow(["study", "python3","auto testing"])
        csvfile.close()

    print("读取csv文件内容")
    with open("csv_data.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print("row 类型：", type(row))
            print(row)

            # 遍历数据项
            for data in row:
                print(data, "  ")
        f.close()

    print("---"*30)
    print("python使用字典方式读写操作")
    # 写
    print("写入数据到csv_dict_data.csv文件中")
    with open("csv_dict_data.csv", "w") as csvdfile:
        # 写csv头
        filenames =["first_name", "last_name"]
        writer = csv.DictWriter(csvdfile, fieldnames=filenames)
        writer.writeheader()
        # 写csv内容
        writer.writerow({"first_name": "Baked",
                         "last_name": "Beans"})
        writer.writerow({"first_name": "Lovely",
                         "last_name": "Spam"})
        writer.writerow({"first_name": "Wonderful",
                         "last_name": "Spam"})
    print("读取csv_dict_data.csv数据")
    with open("csv_dict_data.csv") as csvdfile:
        reader = csv.DictReader(csvdfile)
        for row in reader:
            print(row["first_name"], row["last_name"])