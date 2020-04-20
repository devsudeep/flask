# pip install - e . to install the appliaction
# Nothing changes from how you’ve been running your project so far. FLASK_APP is still set to flaskr and flask run still runs the application, but you can call it from anywhere, not just the flask-tutorial directory.

# Instead of creating a Flask instance globally,
# you will create it inside a function.
# This function is known as the application factory. Any configuration, registration, and other setup the application needs will happen inside the function, then the application will be returned.
# The Application Factory

# TESTING
# pip install pytest coverage

from . import auth
import os

from flask import Flask
from flask_12_flaskr import blog


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    print('...............', app.instance_path, '.................')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return "Hellow world"

    from . import db

    db.init_app(app)
    return app
