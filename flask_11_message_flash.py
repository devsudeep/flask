import os
import sys
from flask.app import Flask
from flask import session, redirect, url_for, request
from markupsafe import escape
from flask.helpers import flash

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

print(sys.getsizeof(session))
@app.route('/')
def index():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
        flash('You are not logged in')
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    flash('You are logged in and redirected to index page')

    if request.method == 'POST':
        session['username'] = request.form['username']
        print(session['username'])
        print(id(session))
        return redirect(url_for('index'))

    return '''
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <ul class=flashes>
        {% for message in messages %}
          <li>{{ message }}</li>
        {% endfor %}
        </ul>
        {% endif %}
        {% endwith %}
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
        '''


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


# How to generate good secret keys

print(os.urandom(16))
