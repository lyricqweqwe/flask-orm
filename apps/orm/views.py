from flask import Blueprint, Flask, render_template

from apps.orm.models import Category

orm = Blueprint('orm', __name__)


@orm.route('/')
def find():
    Category.query.all()
    return 'qq'


@orm.route('/list/<int:page>/<int:size>/')
def pagination_view(page, size):
    pagination = Category.query.all().paginate(page=page, per_page=size, error_out=False)
    # 获取多少页
    print(pagination.pages)
    # 当前页数据
    print(pagination.items)
    # 总条数
    print(pagination.total)
    # 当前页码
    print(pagination.page)
    # 是否有上一页
    print(pagination.has_prev)
    # 是否有下一页
    print(pagination.has_next)
    # 当前页显示多少条数据
    print(pagination.page_num)

    # pagination.iter_pages(left_edge=2, left_current=2,
    #                       right_current=5, right_edge=2)

    # 分页模板
    left_current = 5
    right_current = 5
    if page < 6:
        right_current = 11 - page
    elif pagination.pages - page < 5:
        left_current = 9 - (pagination.pages - page)

    return render_template('pagination.html', pagination=pagination, left_current=left_current,
                           right_current=right_current)


@orm.route('/cate/')
def cate():
    cates = Category.query.all()
    return render_template('cates.html', cates=cates)
