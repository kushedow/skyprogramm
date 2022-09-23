from dao.classes.bookmarks_dao import BookmarksDAO
from dao.classes.comments_dao import CommentDAO
from dao.classes.new_post_dao import NewPostsDAO
from dao.classes.posts_dao import PostsDAO
from service.bookmark import BookmarkService
from service.comment import CommentService
from service.new_post import NewPostService
from service.post import PostService

from setup_db import db

posts_dao = PostsDAO(session=db.session)
new_post_dao = NewPostsDAO(session=db.session)
comments_dao = CommentDAO(session=db.session)
bookmarks_dao = BookmarksDAO(session=db.session)

post_services = PostService(dao=posts_dao)
new_post_services = NewPostService(dao=new_post_dao)
comments_services = CommentService(dao=comments_dao)
bookmarks_services = BookmarkService(dao=bookmarks_dao)
