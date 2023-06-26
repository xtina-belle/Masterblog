import dataclasses
import json

from DB.post_dto import PostDto


class BlogPostsDB:
    def __init__(self, blog_posts_db):
        self.blog_posts_db = blog_posts_db
        self._posts = []

    def setup(self):
        with open(self.blog_posts_db, "r", encoding="utf-8") as file:
            for post in json.load(file):
                self._posts.append(PostDto(*post.values()))

    def _flush_data(self):
        with open(self.blog_posts_db, "w", encoding="utf-8") as file:
            data = [dataclasses.asdict(post) for post in self._posts]
            json.dump(data, file, indent=4)

    def get_blog_posts(self):
        return self._posts

    def get_post(self, post_id):
        for post in self._posts:
            if post.id_ == post_id:
                return post

    def add_post(self, post: PostDto):
        self._posts.append(post)
        self._flush_data()

    def delete_post(self, post_id):
        post = self.get_post(post_id)
        self._posts.remove(post)
        self._flush_data()

    def update_post(self, post_id, title, content):
        post = self.get_post(post_id)
        post.title = title
        post.content = content
        self._flush_data()

    def like_post(self, post_id):
        post = self.get_post(post_id)
        post.like += 1
        self._flush_data()
