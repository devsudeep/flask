from flask import abort, redirect, url_for, render_template
from flask.app import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


@app.errorhandler(404)
def page_not_found_error(error):
    print(error)
    return render_template('page_not_found.html'), 404

