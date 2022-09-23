from dao.models.post import Post


class NewPostsDAO:

    def __init__(self, session):
        self.session = session

    def add_post(self, post):
        """ Добавляет фильм методом POST """
        new_post = Post(**post)
        self.session.add(new_post)
        self.session.commit()
        return new_post
