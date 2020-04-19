# https: // pythonspot.com/login-authentication-with-flask/

from flask import request, render_template
from flask import Flask

from flask_login import login_user, log_the_user_in
app = Flask(__name__)


@app.route('/login', method=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if login_user(request.form['username'], request.form['password']):
            return login_user(request.form['username'])
        else:
            error = 'Invalid username and password'
    return render_template('login.html', error=error)
