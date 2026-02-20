from flask import Blueprint, render_template, request, flash
from flask_login import  login_required, current_user #restricting user to access home page without logging in

views = Blueprint("views", __name__)
 
#i forget to commit this section
@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", user=current_user.username)


@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        test=request.form.get('text')

        if not text:
            flash('post cannot be empty', category='error')
        else:
            flash("post created!", category='success')

    return render_template('create_post.html', user=current_user)