from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import  login_required, current_user #restricting user to access home page without logging in
from .models import Post
from . import db

views = Blueprint("views", __name__)
 
#i forget to commit this section
@views.route("/")
@views.route("/home")
@login_required
def home():
    posts = Post.query.all()
    return render_template("home.html", user=current_user.username, posts=posts)


@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')

        if not text:
            flash('post cannot be empty', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("post created!", category='success')
            return redirect(url_for('views.home'))    

    return render_template('create_post.html', user=current_user)