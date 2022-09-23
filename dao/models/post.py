# from dao.models.bookmark import Bookmark
from setup_db import db
# from dao.models.comment import CommentSchema


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    poster_name = db.Column(db.String(10))
    poster_avatar = db.Column(db.String(100))
    pic = db.Column(db.String(255))
    content = db.Column(db.String(), nullable=False)
    views_count = db.Column(db.Integer)
    likes_count = db.Column(db.Integer)


    bookmark = db.relationship('Bookmark', back_populates="post")


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, nullable=False)
    commenter_name = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)


class Bookmark(db.Model):
    __tablename__ = 'bookmarks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.ForeignKey(Post.id))
    post = db.relationship(Post)

# class PostSchema(Schema):
#     poster_name = fields.Str()
#     poster_avatar = fields.Str()
#     pic = fields.Str()
#     content = Column(String())
#     views_count = Column(Integer)
#     likes_count = Column(Integer)
#     comment = fields.Nested(Type[CommentSchema], many=True)
