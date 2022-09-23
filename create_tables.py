import json
from typing import Union

from config import Config
from app import db
from dao.models.post import Post, Comment, Bookmark
# from dao.models.bookmark import


def read_json(DATA_PATH: str, encoding: str = "utf-8") -> Union[list, dict]:
    with open(DATA_PATH, encoding=encoding) as f:
        return json.load(f)


post = [Post(**post_data) for post_data in read_json(Config.DATA_PATH)]
comment = [Comment(**comment_data) for comment_data in read_json(Config.COMMAENTS_PATH)]

# Закидываем модели в сессию
db.session.add_all(post)
db.session.add_all(comment)
#
# Пишем в базу изменения
db.session.commit()

print("Данные успешно загружены")
