from simple_blog import app, db
from simple_blog.models import User, Blog
import json

@app.route('/')
def index():
    return 'hello world!'

@app.route('/user/<int:user_id>')
def get_user_info(user_id):
    user = User.query.filter_by(id=user_id).first()
    # just test
    if user is None:
        return "Not existed user!"
    data = {"id": user.id, "user_name": user.user_name}
    return json.dumps(data), 200, {"Content-Type":"application/json"}

@app.route('/blog/<int:blog_id>')
def get_blog_info(blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    # just test
    if blog is None:
        return "Not existed blog!"
    data = {"id": blog.id, "title": blog.title, "content": blog.content}
    return json.dumps(data), 200, {"Content-Type":"application/json"}

