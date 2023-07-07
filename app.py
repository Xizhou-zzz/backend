from flask import Flask, render_template, send_from_directory, redirect, url_for, request

app = Flask(__name__)


# 定义路由，发送Vue项目的静态文件
# @app.route('/index.html')
# def index():
#     return render_template('')


@app.route('/<path:path>')
def serve_static(path):
    print(path)
    return send_from_directory('frontend/dist', path)

@app.route('/')
def index():
    return redirect('index.html')


@app.route('/api/login', methods=['POST'])
def process_data():
    # 获取前端传输的数据
    data = request.json  # 假设数据是以JSON格式传输
    # 或者使用 request.form 来获取表单数据

    # 在这里对接收到的数据进行处理
    # ...
    print(data)
    # 返回响应给前端
    return 'Data received and processed successfully'


if __name__ == '__main__':
    app.run()