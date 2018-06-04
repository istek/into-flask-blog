from flask import Flask
from flask import render_template, request, url_for, redirect
from sqlalchemy import desc
from database import session
from models import Blog


app = Flask(__name__)


@app.route('/')
def index():
    blog_title = '我的博客'
    db_session = session()
    allblog = db_session.query(Blog).order_by(desc(Blog.post_date)).all()
    return render_template('index.html',
                           blog_title=blog_title, allblog=allblog)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<post_id>')
def post(post_id):
    db_session = session()
    entry = db_session.query(Blog).filter(Blog.id == post_id).one()
    return render_template('post.html', entry=entry)


@app.route('/newpost', methods=['post'])
def newpost():
    if request.method == 'POST':
        db_session = session()
        title = request.form['title']
        catagory = request.form['catagory']
        auther = request.form['auther']
        content = request.form['content']
        entry = Blog(title=title, catagory=catagory,
                     auther=auther, content=content)
        db_session.add(entry)
        db_session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
