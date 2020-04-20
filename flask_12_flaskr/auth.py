# Blueprints and Views
# A Blueprint is a way to organize a group of related views and other code.
# Rather than registering views and other code directly with an application,
# they are registered with a blueprint. Then the blueprint is registered
# with the application when it is available in the factory function.

import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash
from flask_12_flaskr.db import get_db
from marshal import dump

bp = Blueprint('auth', __name__, url_prefix='/auth')
# add the blueprint to __init__ app object
# The authentication blueprint will have views to register new users and to log in and log out.


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # dump(request.form)
        db = get_db()
        error = None
        if not username:
            error = 'User name is required'
        elif not password:
            error = 'Password is required'
        elif db.execute(
                'SELECT id from user where username = ?', (username,)).fetchone() is not None:
            error = 'User {} is already registered'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    print(url_for('auth.register'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM USER WHERE username = ?', (username, )
        ).fetchone()

        if user is None:
            error = 'Incorrect username'
        elif not check_password_hash(user['password'], password):
            error = ' Incorrect Password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('auth.login'))

        flash(error)
    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    print('Gid..............', id(g))
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM USER WHERE id = ?', (user_id, )
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


# Require Authentication in Other Views
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwrgs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwrgs)
    return wrapped_view
