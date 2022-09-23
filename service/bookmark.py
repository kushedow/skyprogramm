from dao.classes.bookmarks_dao import BookmarksDAO


class BookmarkService:
    def __init__(self, dao: BookmarksDAO):
        self.dao = dao

    def get_all_bookmarks(self):
        return self.dao.get_bookmarks()

    def add_bookmarks(self, post_id: int) -> object:
        return self.dao.add_bookmark(post_id)

    def del_bookmark(self, post_id):
        return self.dao.del_bookmark(post_id)
