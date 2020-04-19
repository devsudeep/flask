from flask import Flask, url_for
from markupsafe import escape
from flask import request
import time

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    print('POST') if request.method == 'POST' else print("GET")
    print(dir(request))
    # try:

    #     for v in dir(request):
    #         print(getattr(request, v))
    #         # time.sleep(1)

    # except Exception:
    #     print('error')
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


@app.route('/about/1/2/3')
def about():
    return 'about us'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='dow'))
    print(url_for('about'))
    print(url_for('static', filename='style.css'))
