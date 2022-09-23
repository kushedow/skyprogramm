from dao.models.post import Post


class PostsDAO:

    def __init__(self, session):
        self.session = session

    def get_posts_all(self):
        """Возвращает все посты"""
        return self.session.query(Post).offset(5).all()

    def get_posts_by_user(self, poster_name):
        """ Возвращает посты определенного пользователя по имени"""
        return self.session.query(Post).filter(Post.poster_name == poster_name).all()

    def get_post_by_pk(self, pk):
        """Возвращает один пост по его id"""
        return self.session.query(Post).filter(Post.id == pk).all()
