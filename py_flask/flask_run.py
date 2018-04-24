#-*- coding:utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/api')
def hello_world():
    return 'Hello World!'


# <username>可作为命名参数传递到行数
@ app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

# 使用转换器（int, float, path）
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

# HTTP方法（GET、HEAD、POST、PUT、DELETE、OPTIONS）
@app.route('/login', methods=['GET', 'POST'])
def login():
    pass
    '''
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
    '''


if __name__ == '__main__':
    app.run(debug=True)