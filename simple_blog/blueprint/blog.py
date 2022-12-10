# -*- coding: utf-8 -*- 
from flask import Blueprint,request, current_app, render_template
from simple_blog.models import Blog

blog_bp =Blueprint('blog_bp', __name__)

@blog_bp.route('/', methods = ['GET'])
@blog_bp.route('/index/', methods=['GET'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Blog.query.order_by(Blog.is_top.desc()).paginate(page=page, per_page=current_app.config['SIMPLE_BLOG_PER_PAGE'])
    blogs = pagination.items
    return render_template('index.html', blogs=blogs, pagination = pagination)