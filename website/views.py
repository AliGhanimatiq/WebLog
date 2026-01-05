from flask import Blueprint, render_template
from flask_login import  login_required, current_user #restricting user to access home page without logging in

views = Blueprint("views", __name__)
 
#i forget to commit this section
@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", user=current_user.username) 