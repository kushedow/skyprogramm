from flask import Blueprint, render_template, request

from implemented import post_services

search = Blueprint('search', __name__, template_folder="templates")


@search.route("/search/")
def page_search():
    """ Реализует поиск по совпадениям в словах в постах"""
    word = request.args.get('word')
    posts = post_services.get_search_(word)
    return render_template("search.html",
                           posts=posts,
                           count_post=len(posts),
                           word=word)


@search.route("/tag/<tagname>/")
def page_tag(tagname):
    """ Реализует переход по тегам"""
    posts = post_services.get_search_("#" + tagname)
    for post in posts:
        if tagname.lower() in post.content.lower():
            return render_template("tag.html", tagnames=post_services.get_tag_names(tagname), search_tag=tagname)
