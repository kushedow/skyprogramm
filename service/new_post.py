from dao.classes.new_post_dao import NewPostsDAO


class NewPostService:
    """ Добавляет новый пост"""

    def __init__(self, dao: NewPostsDAO):
        self.dao = dao

    def add_new_post(self, post):
        return self.dao.add_post(post)

    @classmethod
    def loading_error_json(cls, DATA_PATH):
        if not DATA_PATH:
            return "Файл .json отсутствует или не хочет превращаться в список"

    @classmethod
    def loading_error_pic(cls, pic):
        if not pic:
            raise FileNotFoundError("Ошибка загрузки из-за отсутствия ФАЙЛА ")

    @classmethod
    def loading_error_content(cls, content):
        if not content:
            raise TypeError("Введите описание поста")

    @classmethod
    def loading_error_poster_name(cls, poster_name):
        if not poster_name:
            raise TypeError("Введите ваше имя")

    @classmethod
    def invalid_file_type(cls, filename, ALLOWED_EXTENSIONS):
        extension = filename.split(".")[-1]
        if extension not in ALLOWED_EXTENSIONS:
            raise TypeError(
                f"Загруженный файл - {extension} (Доступные расширение 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif')")
