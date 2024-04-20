from flask import Blueprint,render_template,request,redirect,url_for
from models import Post,Tag
from forms import PostForm,TagForm
from app import db


posts = Blueprint('posts',__name__,template_folder='templates',url_prefix='/blog')


@posts.route('/posts_list',methods=['GET','POST'])
def posts_list():
    post_form = PostForm(request.form)
    tagForm = TagForm(request.form)
    
    p = Post(**request.form)
    db.session.add(p)
    
    db.session.commit()
    
    posts = Post.query.all()
    tags = Tag.query.all()
    return render_template('posts_list.html',post=posts, tags=tags, tagForm=tagForm, form=post_form )

@posts.route('/postBlog')
def postBlog():
    post_form = PostForm(request.form)
    print(post_form)
    p = Post(**request.form)
    # p = Post(title=form.get('title'),body=form.get('body'),slug=form.get('slug'))
    db.session.add(p)
    db.session.commit()
    # form = PostForm()
    return render_template('posts_list.html',form=post_form)

@posts.route('/tagPost')
def tagPost():
    tagForm = TagForm(request.form)
    
    t = Tag(**request.form)
    db.session.add(t)
    db.session.commit()
    tags = Tag.query.all()
    return render_template('tag.html',tagForm=tagForm,tags= tags)