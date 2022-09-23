from flask import Blueprint, render_template, redirect

from implemented import bookmarks_services, post_services

bookmarks = Blueprint('bookmarks', __name__, template_folder="templates")


@bookmarks.route("/bookmarks/")
def all_bookmark():
    """Выводит все добавленые закладки"""
    bookmarks = bookmarks_services.get_all_bookmarks()  # Возращает все добавленые закладки
    post = post_services.get_one_pk(bookmarks)  # Возвращает один пост по его id
    return render_template("bookmarks.html", all_bookmarks=bookmarks)


@bookmarks.route("/bookmarks/add/<post_id>/")
def bookmarks_add_post(post_id):
    """ Добавляет посты в закладки."""
    bookmarks_services.add_bookmarks(post_id)
    return redirect("/", code=302)

# @app.route('/bookmarks/delete/<int:post_id>')
# def page_bookmarks_delete(post_id):
#     """  Удаляет посты из закладок"""
#     posts = data_posts.get_post_by_pk(post_id)
#     bookmarks.del_bookmark(posts)
#     return redirect("/", code=302)
#
#
