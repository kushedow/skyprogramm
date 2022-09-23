from dao.classes.posts_dao import PostsDAO


class PostService:

    def __init__(self, dao: PostsDAO):
        self.dao = dao

    def get_posts(self):
        return self.dao.get_posts_all()

    def get_by_name(self, poster_name):
        return self.dao.get_posts_by_user(poster_name)

    def get_one_pk(self, post_id):
        posts = self.dao.get_post_by_pk(post_id)
        content_with_links = []
        for post in posts:
            words = post.content.split()  # Сохраняем текст тут
            for word in words:
                if word.startswith("#"):
                    content_with_links.append(f'<a href="/tag/{word[1:]}" class="item__tag">{word}</a>')
                else:
                    content_with_links.append(word)
            post.content = " ".join(content_with_links)
            return posts

    def get_search_(self, content) -> list:
        """ Возвращает список постов по ключевому слову"""
        if content in (" ", ""):
            return []
        current_posts = []
        for post in self.get_posts():
            if str(content).lower() in post.content.lower():
                current_posts.append(post)
        return current_posts

    def get_tag_names(self, tagname):
        """ Возвращает посты по тэгами"""
        tag = []
        for tag_post in self.get_search_(tagname):
            if tagname in tag_post.content:
                tag.append(tag_post)
        return tag


