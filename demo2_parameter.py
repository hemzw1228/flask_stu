# 1.导入Flask
from flask import Flask

# 2.创建Flask实例
app = Flask(__name__,   # 1根据该参数，找到模块根目录绝对路径，2 找到静态文件夹和模板文件夹路径
            static_url_path='/static',  # 当static_url_path 默认None，实际则与static_folder相等
            static_folder='static',  # 设置静态文件夹名字， 默认static
            template_folder='templates'  # 设置模板文件夹名字
            )


# 3.设置路由
@app.route('/')
def index():
    return "Flask 常用参数，请看代码注释"


# 4.运行
if __name__ == '__main__':
    app.run()
