from markupsafe import Markup
from flask import render_template
from flask.app import Flask

app = Flask(__name__)
app.debug = True


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


print(Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>')
print(Markup.escape('<blink>hacker</blink>'))
print(Markup('<em>Marked up</em> &raquo; HTML').striptags())
print(globals())
