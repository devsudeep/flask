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
from flask_debugtoolbar import DebugToolbarExtension

from flask import Flask, template_rendered, before_render_template, request_started, g
from flask_12_flaskr import blog
import flask_profiler
import blinker
from werkzeug import Response
import random


def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    print(__name__)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'

    print('...............', app.instance_path, '.................')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
    toolbar = DebugToolbarExtension(app)
    # app.config["flask_profiler"] = {
    #     "enabled": app.config["DEBUG"],
    #     "storage": {
    #         "engine": "sqlite"
    #     },
    #     "basicAuth": {
    #         "enabled": False,
    #         "username": "sudeep",
    #         "password": "sudeep"
    #     },
    #     "ignore": [
    #         "^/static/.*"
    #     ]
    # }
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route
    def test():
        return "test"

    @app.route('/hello')
    def hello():
        return "Hellow world"

    def test():
        return "test"
    app.add_url_rule('/test', 'test', test)

    def log_template_renders(sender, template, context, **extra):
        sender.logger.debug('Rendering template "%s" with context %s',
                            template.name or 'string template',
                            context)

    template_rendered.connect(log_template_renders, app)
    before_render_template.connect(log_template_renders, app)

    def request_finishing(sender):
        print("request finishing")
        print(sender)
        req = app.request_context
        print(req)

    def after_request(resp):
        print(dir(resp))

    # resp = Response()

    # app.after_request(after_request)
    # app.teardown_request(request_finishing)

    @request_started.connect_via(app)
    def log_request(sender, **extra):
        g.rand = os.urandom(42)
        print("**********************", g.rand, "**********************")
        print(sender, 'request received..............---------==')

        sender.logger.debug('Request context is set up')
    request_started.connect(log_request, app)
    from . import db
    app.env = 'development'
    db.init_app(app)

    @template_rendered.connect_via(app)
    def when_template_rendered(sender, template, context, **extra):
        print('Template %s is rendered with %s' % (template.name, context))
    return app
