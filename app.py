from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


# 定义路由，发送Vue项目的静态文件
# @app.route('/index.html')
# def index():
#     return render_template('')


@app.route('/<path:path>')
def serve_static(path):
    print(path)
    return send_from_directory('frontend/dist', path)


if __name__ == '__main__':
    app.run(default_url='/index.html')