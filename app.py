from flask import Flask
from flask_restx import Api

from api.api import posts_ns
from config import Config

from dao.models.post import *
from views_blueprint.bookmarks.bookmarks import bookmarks
from views_blueprint.error.error import page_error
from views_blueprint.posts.posts import post
from views_blueprint.search.search import search

from views_blueprint.users.users import user


def create_app(config_object):
    """  Функция создания основного объекта app """
    app = Flask(__name__)
    app.register_blueprint(post)
    app.register_blueprint(search)
    app.register_blueprint(page_error)
    app.register_blueprint(user)
    app.register_blueprint(bookmarks)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """ Функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx) """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(posts_ns)
    create_data(app, db)


def create_data(app, db):
    app.app_context().push()
    db.create_all()


app = create_app(Config())

if __name__ == '__main__':
    app.run()
