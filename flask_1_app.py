import dis
from flask import Flask
from markupsafe import escape
from urllib3 import request
app = Flask(__name__)
print(__name__)


print(dis.dis(app))
print(type(app))
# print(dir(app))
# for v in dir(app):
#     print(v)


@app.route('/')
def hello_world():
    return "hello world"


@app.route('/user/<username>')
def show_user_profile(username):
    print(request)
    print(dir(request))
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)


# The canonical URL for the projects endpoint has a trailing slash. It’s similar to a folder in a file system. If you access the URL without a trailing slash, Flask redirects you to the canonical URL with the trailing slash.

# The canonical URL for the about endpoint does not have a trailing slash. It’s similar to the pathname of a file. Accessing the URL with a trailing slash produces a 404 “Not Found” error. This helps keep URLs unique for these resources, which helps search engines avoid indexing the same page twice.
@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


# URL Building


# app.run(debug=True)
