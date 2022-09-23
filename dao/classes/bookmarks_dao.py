from dao.models.post import Bookmark, Post


class BookmarksDAO:

    def __init__(self, session):
        self.session = session

    def get_bookmarks(self):
        """Возращает все закладки"""
        return self.session.query(Bookmark).all()

    def add_bookmark(self, post_id: int):
        """ Добавляет закладку"""
        bookmarks = self.get_bookmarks()  # Возращает все закладки
        if post_id in bookmarks or not post_id:
            return
        else:
            bookmark = Bookmark(post_id=post_id)
            self.session.add(bookmark)
            self.session.commit()
            return bookmarks

    def del_bookmark(self, post_id):
        """ Удаляет закладку"""
        get_bookmark = self.get_bookmarks()
        if post_id not in get_bookmark or not post_id:
            return
        get_bookmark.remove(post_id)
        self.session.delete(get_bookmark)
        self.session.commit()
