# from setup_db import db
# #
# #
# class Bookmark(db.Model):
#     __tablename__ = 'bookmarks'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     post_id = db.Column(db.Integer, db.ForeignKey("Post.id"))
#     post = db.relationship("Post")

#     poster_name = db.Column(db.String(10))
#     poster_avatar = db.Column(db.String(100))
#     pic = db.Column(db.String(255))
#     content = db.Column(db.String(), nullable=False)
#     views_count = db.Column(db.Integer)
#     likes_count = db.Column(db.Integer)
#
