from flask import render_template, request, Blueprint
from webseite.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    # page = request.args.get('page', 1, type=int)
    # posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home/index.html')


@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('posts/home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('home/impressum.html', title='About')
