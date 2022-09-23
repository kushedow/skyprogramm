class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///skypogram.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}  # Нормальное отображение русских символов
    DATA_PATH = 'data/data.json'
    COMMAENTS_PATH = 'data/comments.json'
    BOOKMARKS_PATH = 'data/bookmarks.json'
    UPLOAD_FOLDER = "./uploads/images/"
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 2048 * 2048
