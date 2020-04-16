from flask import Flask
app = Flask(__name__)
print(__name__)

print(type(app))
print(dir(app))


@app.route('/')
def hello_world():
    return "hello world"
