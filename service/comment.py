from dao.classes.comments_dao import CommentDAO


class CommentService:
    def __init__(self, dao: CommentDAO):
        self.dao = dao

    def get_comments_all(self):
        return self.dao.get_comments()

    def get_comments_id(self, comment_id):
        return self.dao.get_comments_by_post_id(comment_id)
