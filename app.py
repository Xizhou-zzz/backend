from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.template_folder = '/static/src'


# 定义路由，发送Vue项目的静态文件
# @app.route('/')
# def index():
#     return render_template('App.vue')


@app.route('/<path:path>')
def serve_static(path):
    print(path)
    return send_from_directory('dist', f'{path}')


if __name__ == '__main__':
    app.run()