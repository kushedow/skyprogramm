import os
from flask_restx import Resource, Namespace
from flask import jsonify
import logging

from implemented import post_services

path = os.path.join("logs", "api.log")

# Логирование
logger_api = logging.getLogger("api")  # Создаем логгер
file_handler = logging.FileHandler(path)  # Записываем логи в файл

logger_api.setLevel("INFO")  # Уровень записи в логи
formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")  # В каком формате будет запись

file_handler.setFormatter(formatter_api)  # применяем формат к логам
logger_api.addHandler(file_handler)  # записываем в журнал

posts_ns = Namespace('api/post')


# TODO: создать схему

@posts_ns.route("/")
class PostApi(Resource):
    def page_post_form(self):
        """возвращает полный список постов в виде JSON-списка"""
        logger_api.info("запрос всех постов")
        all_posts = post_services.get_posts()
        return jsonify(all_posts)


@posts_ns.route("/<int:post_id>/")
class PostApi(Resource):
    def page_post_pk(seld, post_id):
        """возвращает один пост в виде JSON-словаря."""
        logger_api.info(f"запрос постов по {post_id}")
        get_post = post_services.get_one_pk(post_id)
        return jsonify(get_post)
