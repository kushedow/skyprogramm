from flask import Blueprint, render_template

from implemented import post_services

user = Blueprint('user', __name__, template_folder="templates", static_folder="static")


@user.route("/users/<username>/")
def page_user(username):
    """ Реализует вывод по пользователю """
    return render_template("user-feed.html", user_posts=post_services.get_by_name(username))
