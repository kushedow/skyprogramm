from flask import Blueprint, render_template, request, send_from_directory
from implemented import comments_services, new_post_services, bookmarks_services
from config import Config
from implemented import post_services

post = Blueprint('post', __name__, template_folder="templates", static_folder="static")


@post.route('/')
def all_posts():
    """Реализует ленту до 5 постов"""
    return render_template("index.html",
                           all_post=post_services.get_posts(),
                           count_comment=len(bookmarks_services.get_all_bookmarks()))


@post.route("/post/<int:post_id>/")
def one_post(post_id):
    """ Реализует просмотр поста"""
    post = post_services.get_one_pk(post_id)
    return render_template("post.html", posts=comments_services.get_comments_id(post_id),
                           count_comment=len(comments_services.get_comments_id(post_id)),
                           post=post)


@post.route("/post/")
def page_post_form():
    """Возвращает форму добавления поста"""
    return render_template("post_form.html")


@post.route("/post/new/", methods=["POST"])
def page_post_upload():
    picture_file = request.files.get("picture")
    if new_post_services.loading_error_pic(picture_file):
        return FileNotFoundError, 501
    filename = picture_file.filename
    if new_post_services.invalid_file_type(filename, Config.ALLOWED_EXTENSIONS):
        return TypeError, 503
    picture_file.save(f"{Config.UPLOAD_FOLDER}/{filename}")
    contents = request.values.get('content')
    if new_post_services.loading_error_content(contents):
        return ValueError, 502
    poster_name = request.form['username']
    if new_post_services.loading_error_poster_name(poster_name):
        return ValueError, 502
    new_post_ = {
        "pic": f'/uploads/{filename}',
        "content": contents,
        "poster_name": poster_name
    }
    new_post_services.add_new_post(new_post_)
    return render_template("post_uploaded.html",
                           filename=filename,
                           contents=contents,
                           poster_name=poster_name)


@post.route("/uploads/<path:path>", methods=["GET", "POST"])
def static_dir(path):
    return send_from_directory(Config.UPLOAD_FOLDER, path)
