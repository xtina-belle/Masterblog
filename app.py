from flask import Flask, render_template, request, redirect, url_for

from DB.blog_posts_db import BlogPostsDB, PostDto

BLOG_POSTS_DB = "DB/blog_posts.json"

blog_posts_db = BlogPostsDB(BLOG_POSTS_DB)
blog_posts_db.setup()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", posts=blog_posts_db.get_blog_posts())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        _id = max([post.id_ for post in blog_posts_db.get_blog_posts()], default=0) + 1
        author = "Joe Doe"
        title = request.form.get("title")
        content = request.form.get("content")
        blog_posts_db.add_post(PostDto(_id, author, title, content))
        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
    blog_posts_db.delete_post(post_id)
    return redirect(url_for("index"))


@app.route("/like/<int:post_id>", methods=["POST"])
def like_post(post_id):
    blog_posts_db.like_post(post_id)
    return redirect(url_for("index"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    post = blog_posts_db.get_post(post_id)
    if not post:
        return "Post not found", 404

    if request.method == 'POST':
        title = request.form.get("title")
        content = request.form.get("content")
        blog_posts_db.update_post(post_id, title, content)
        return redirect(url_for("index"))

    return render_template('update.html', post=post)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
