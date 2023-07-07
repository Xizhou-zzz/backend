from flask import Flask, render_template, send_from_directory, redirect, url_for, jsonify, request

app = Flask(__name__)


@app.route('/<path:path>')
def serve_static(path):
    print(path)
    return send_from_directory('frontend/dist', path)


@app.route('/')
def index():
    return redirect('index.html')


@app.route('/api/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    # 在这里你可以将前端传递的用户名和密码与数据库内容进行对比
    # 这里只做示例，直接返回一个登录成功的信息
    if username == 'admin' and password == 'password':
        print(username, password)
        print("OK")
        return jsonify(message='登录成功')
    else:
        print(username, password)
        print("not OK")
        return jsonify(message='用户名或密码错误')


@app.route('/api/Register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']


if __name__ == '__main__':
    app.run()