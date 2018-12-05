from flask import Blueprint, render_template, request

from apps.ext import db
from apps.user.models import User

user = Blueprint('user', __name__)


@user.route('/add/')
def add():
    # user = User(username='娇娇')
    # db.session.add(user)
    # db.session.commit()
    # 批量添加
    db.session.add_all([User(username='宫地蓝', price=9.99), User(username='彩美旬果', price=9.99)])
    db.session.commit()
    return '添加操作'


@user.route('/find/')
def find():
    users = User.query.all()
    return render_template('users.html', users=users)


@user.route('/detail/')
def detail():
    uid = request.args.get('uid')
    user = User.query.get(uid)
    return render_template('detail.html',user=user)