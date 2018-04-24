#-*- coding:utf-8 -*-

"""
基于flask实现HTTP的GET、POST、HEAD方法
"""
import random
import time

from flask import Flask, jsonify, request, Response

app = Flask(__name__)
"""
所有接口都返回json串
所有json串对应的value都是随机的
"""

# 生成随机字符串
def random_str():
    # 待选随机数据
    data = "1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*()+=-"
    # 用时间来做随机播种
    random.seed(time.time())
    # 随机选取数据
    sa = []
    for i in range(8):
        sa.append(random.choice(data))
    salt = ''.join(sa)
    return salt

# 构建response
def make_response():
    content = '{"result": "%s", "data":"%s"}' % (random_str(),
                                                 random_str())
    resp = Response(content)
    resp.headers["Access-Control-Origin"] = '*'
    return resp

# HTTP GET
@app.route("/query", methods=["GET"])
def query():
    return jsonify(
        username = random_str(),
        password = random_str()
    )

# HTTP POST
@app.route("/update", methods=["POST"])
def update():
    return make_response()

# HTTP delete
@app.route("/delete", methods=["DELETE"])
def delete():
    return make_response()

# HTTP head
@app.route("/head", methods=["HEAD"])
def head():
    return make_response()

if __name__ == '__main__':
    app.run(debug=True)