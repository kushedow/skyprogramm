# from setup_db import db
#
#
# class Comment(db.Model):
#     __tablename__ = 'comments'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     post_id = db.Column(db.Integer, nullable=False)
#     commenter_name = db.Column(db.String, nullable=False)
#     comment = db.Column(db.String, nullable=False)

# #
# class CommentSchema(Schema):
#     post_id = fields.Str()
#     commenter_name = fields.Str()
#     comment = fields.Str()
