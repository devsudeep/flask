from flask import request
from flask.app import Flask

app = Flask(__name__)


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='dow'))
#     print(url_for('about'))
#     print(url_for('static', filename='style.css'))

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

# The other possibility is passing a whole WSGI environment to the request_context() method:

# with app.request_context(environ):
#     assert request.method == 'POST'
