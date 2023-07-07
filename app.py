from flask import Flask, render_template, send_from_directory, redirect, abort, jsonify, request
from controller import DBcontroller
app = Flask(__name__)


@app.route('/api/login', methods=['POST'])
def login():
    print("收到登录请求")
    username = request.json['username']
    password = request.json['password']
    print(username, password)
    # 进行数据验证，这里仅作示例直接返回结果
    if username == 'admin' and password == 'password':
        result = 'success'
    else:
        result = 'failure'

    return jsonify({'result': result})


@app.route('/Visualize', methods=['GET'])
def visualize():
    db = DBcontroller.Database()
    df = db.select('bikemessage', condition='bikeid = 288841')   # 调用查询方法获取数据（返回一个DataFrame）
    new_df = df.loc[:, ['start_location_x', 'start_location_y']]
    data = new_df.to_dict(orient='records')   # 转换为字典格式
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run()














# @app.route('/<path:path>')
# def serve_static(path):
#     print(path)
#     return send_from_directory('frontend/dist', path)
#
#
# @app.route('/')
# def index():
#     return redirect('index.html')
#
#
# @app.route('/api/login', methods=['POST'])
# def login():
#     username = request.json['username']
#     password = request.json['password']
#
#     # 在这里进行用户身份验证
#     # 假设验证失败
#     if username != 'admin' or password != 'password':
#         response = {
#             'success': False,
#             'message': '登录失败，用户名或密码错误'
#         }
#         return jsonify(response), 401  # 返回 401 状态码表示未授权
#
#     # 假设验证通过，返回成功响应
#     response = {
#         'success': True,
#         'message': '登录成功',
#         'data': {
#             'token': 'your_jwt_token',
#             'username': username,
#         }
#     }
#     return jsonify(response)
#
#
# @app.route('/index.html#/<path:path>')
# def get_data(path):
#     print(path)
#     return
#
#
# @app.route('/api/Register', methods=['POST'])
# def register():
#     username = request.json['username']
#     password = request.json['password']