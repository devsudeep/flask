from flask import request
from flask import make_response, render_template
from flask.app import Flask

app = Flask(__name__)


@app.route('/')
def index():
    username = request.cookies.get('username')
    print(dir(request))
    for v in dir(request):
        print(getattr(request, v, 'Not found..........'))
    return 'cookie value:' + username


@app.route('/login')
def login():
    resp = make_response(render_template('login.html'))
    resp.set_cookie('username', 'sudeep')
    print(dir(resp))
    return resp
