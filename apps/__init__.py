from flask import Flask

from apps.ext import init_ext
from apps.orm.views import orm
from apps.user.views import user

# 入口
def create_app():
    app = Flask(__name__)
    app.debug = True
    init_ext(app)
    # 注册蓝图
    register(app)
    return app


# 注册蓝图对象
def register(app:Flask):
    # 注册用户模块
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(orm)





