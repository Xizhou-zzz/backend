from flask import Flask, jsonify, request
from flask_cors import CORS
from controller import DBcontroller
import pandas as pd
app = Flask(__name__)
CORS(app)
db = DBcontroller.Database()


@app.route('/api/login', methods=['POST'])
def login():
    print("收到登录请求")
    data = request.get_json()
    username = data['username']
    password = data['password']
    df = db.select('usermessage')   # 调用查询方法获取数据（返回一个DataFrame）
    search_value = username
    mask = df['user_name'].isin([search_value])
    if mask.any():
        # 获取目标行的密码
        password_saved = df.loc[mask, 'user_password'].values[0]
        print(f"找到用户名为'{search_value}'，对应的密码为'{password_saved}'")
        if password == password_saved:
            print("允许登录")
            user_class = df.loc[mask, 'user_class'].values[0]
            if user_class == 1:
                result = 'admin'
            else:
                result = 'success'
        else:
            print("拒绝登录")
            result = 'failure'
    else:
        print("未找到该用户名")
        result = 'NOTFOUND'

    return jsonify({'result': result})


@app.route('/api/Register', methods=['POST'])
def register():
    print("收到注册请求")
    data = request.get_json()
    username = data['username']
    password = data['password']
    df = db.select('usermessage')   # 调用查询方法获取数据（返回一个DataFrame）
    search_value = username
    mask = df['user_name'].isin([search_value])
    if mask.any():
        # 获取目标行的密码
        print("用户名已存在")
        result = 'EXIST'
    else:
        print("未找到该用户名")
        db.insert('usermessage', (username, password, 0))
        result = 'NOTFOUND'

    return jsonify({'result': result})


@app.route('/api/Visualone', methods=['GET'])
def visualone():
    print("收到数据请求")
    df = db.select('bikemessage')   # 调用查询方法获取数据（返回一个DataFrame）
    # new_df = new_df.rename(columns={'orderid': 'name', 'userid': 'value'})
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['weekday'] = df['start_time'].dt.weekday
    # 按星期几分组并计算每个组的数量
    weekday_count = df.groupby('weekday').size().reset_index(name='count')
    # 将结果保存为DataFrame数据流
    weekday_count_stream = weekday_count.to_json(orient='records')
    weekday_mapping = {
        0: 'Mon',
        1: 'Tue',
        2: 'Wed',
        3: 'Thu',
        4: 'Fri',
        5: 'Sat',
        6: 'Sun'
    }
    # 将 'weekday' 列的值替换为星期的缩写
    weekday_count['weekday'] = weekday_count['weekday'].replace(weekday_mapping)
    # 打印结果
    weekday_count = weekday_count.rename(columns={'weekday': 'name', 'count': 'value'})
    data = weekday_count.to_dict(orient='records')   # 转换为字典格式
    print(data)
    print("数据请求处理完毕")
    return jsonify(data)


@app.route('/api/Visualtwo', methods=['GET'])
def visualtwo():
    print("收到数据请求")
    df = db.select('bikemessage')   # 调用查询方法获取数据（返回一个DataFrame）
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['hour'] = df['start_time'].dt.hour
    # 创建时间段的标签
    time_labels = ['0:00-0:59', '1:00-1:59', '2:00-2:59', '3:00-3:59',
                   '4:00-4:59', '5:00-5:59', '6:00-6:59', '7:00-7:59',
                   '8:00-8:59', '9:00-9:59', '10:00-10:59', '11:00-11:59',
                   '12:00-12:59', '13:00-13:59', '14:00-14:59', '15:00-15:59',
                   '16:00-16:59', '17:00-17:59', '18:00-18:59', '19:00-19:59',
                   '20:00-20:59', '21:00-21:59', '22:00-22:59', '23:00-23:59']

    # 使用cut()函数对时间进行分段，并计算每个时段的数量
    time_count = pd.cut(df['hour'],
                        bins=range(0, 25),
                        labels=time_labels,
                        include_lowest=True).value_counts().sort_index().reset_index()
    time_count.columns = ['time_range', 'count']
    time_count = time_count.rename(columns={'time_range': 'name', 'count': 'value'})
    # 将结果保存为DataFrame数据流
    data = time_count.to_dict(orient='records')   # 转换为字典格式
    print("数据请求处理完毕")
    return jsonify(data)


@app.route('/api/getUsers', methods=['GET'])
def users():
    print("收到用户数据请求")
    df = db.select('usermessage')   # 取得dataframe数据
    df = df.rename(columns={'user_name': 'username', 'user_password': 'password', 'user_class': 'typology'})
    data = df.to_dict(orient='records')
    print(data)
    return jsonify(data)


@app.route('/api/deleteRow', methods=['POST'])
def delete():
    print("收到删除用户数据请求")
    data_from_frontend = request.get_json()
    username = data_from_frontend['username']
    db.delete('usermessage', f"user_name='{username}'")   # 取得dataframe数据
    result = "deleted"
    return jsonify(result)


@app.route('/api/addRow', methods=['POST'])
def insert():
    print("收到添加用户数据请求")
    data_from_frontend = request.get_json()
    username = data_from_frontend['name']
    password = data_from_frontend['password']
    typology = data_from_frontend['type']
    result = 'success'
    try:
        db.insert('usermessage', (username, password, int(typology)))
    except Exception as e:  # 捕获到异常，说明出现了主键冲突错误
        if 'PRIMARY' in str(e):
            # 处理主键冲突的情况
            print(f"插入失败，用户名 '{username}' 已存在。")
            result = 'exist'
        else:
            # 处理其他异常
            print("插入失败，发生未知错误:", e)
            result = 'failure'
    print(result)
    return jsonify(result)


@app.route('/api/updateRow', methods=['POST'])
def update():
    print("收到更新用户数据请求")
    data_from_frontend = request.get_json()
    print(data_from_frontend)
    username = data_from_frontend['name']
    password = data_from_frontend['password']
    typology = data_from_frontend['type']
    print(username)
    print(password)
    print(typology)
    result = 'success'
    try:
        db.update('usermessage', 'user_name', username, f"user_name='{username}'")
        db.update('usermessage', 'user_password', password, f"user_name='{username}'")
        db.update('usermessage', 'user_class', int(typology), f"user_name='{username}'")
    except Exception as e:  # 捕获到异常，说明出现了主键冲突错误
        if 'PRIMARY' in str(e):
            # 处理主键冲突的情况
            print(f"更改失败，用户名 '{username}' 已存在。")
            result = 'exist'
        else:
            # 处理其他异常
            print("更新失败，发生未知错误:", e)
            result = 'failure'
    print(result)
    return jsonify(result)


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