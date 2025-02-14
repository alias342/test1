from flask import Flask, render_template
from post import Post
import os

blogs = Post()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=blogs.get_blogs())

port = int(os.environ.get("PORT", 10000))

@app.route('/post/<int:blog_id>')
def blog_page(blog_id):
    return render_template("post.html", blog=blogs.specific_blog(blog_id))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=False)
