from flask import Flask, render_template, send_from_directory, redirect, abort, jsonify, request

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

    # 在这里进行用户身份验证
    # 假设验证失败
    if username != 'admin' or password != 'password':
        response = {
            'success': False,
            'message': '登录失败，用户名或密码错误'
        }
        return jsonify(response), 401  # 返回 401 状态码表示未授权

    # 假设验证通过，返回成功响应
    response = {
        'success': True,
        'message': '登录成功',
        'data': {
            'token': 'your_jwt_token',
            'username': username,
        }
    }
    return jsonify(response)


@app.route('/api/Register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']


if __name__ == '__main__':
    app.run()