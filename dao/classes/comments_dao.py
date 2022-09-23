from dao.models.post import Comment


class CommentDAO:

    def __init__(self, session):
        self.session = session

    def get_comments(self):
        """Возвращает ВСЕ комментарии к постам"""
        return self.session.query(Comment).all()

    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии определенного поста"""
        return self.session.query(Comment).filter(Comment.post_id == post_id).all()
