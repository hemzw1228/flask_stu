# 1.导入flask
from flask import Flask

# 2.创建实例
app = Flask(__name__,static_folder='mzw')


# 3.添加路由
@app.route('/')
def index():
    return "hello world"

# 4.运行
if __name__ == '__main__':
    app.run()
