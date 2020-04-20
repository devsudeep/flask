
https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

```bash

$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/


Alternatively you can use python -m flask:

$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
```
# Externally Visible Server
```bash
$ flask run --host=0.0.0.0
```


# To install as package

pip install -e . as package

to test add PYTHONPATH=. env variable

# Deploy to Production

```shell
pip install wheel

python setup.py bdist_wheel
find the buidl in dist/flaskr-1.0.0-py3-none-any.whl


Copy this file to another machine, set up a new virtualenv, then install the file with pip.

```shell
$ pip install flaskr-1.0.0-py3-none-any.whl
$ export FLASK_APP=flaskr
$ flask init-db

```
When Flask detects that it’s installed (not in editable mode), it uses a different directory for the instance folder. You can find it at venv/var/flaskr-instance instead.

# Configure the Secret Key
```shell
$ python -c 'import os; print(os.urandom(16))'

b'_5#y2L"F4Q8z\n\xec]/'
```
Create the config.py file in the instance folder, which the factory will read from if it exists. Copy the generated value into it.

venv/var/flaskr-instance/config.py
SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'


# Run with a Production Server

