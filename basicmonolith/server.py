# run the following in your terminal for django:
# $ django-admin startproject config .
# that will generate the scaffolding for a standard project

# for flask:
# $ python3 -m venv venv
# $ source venv/bin/activate
# $ pip3 install -r requirements.txt
# $ export FLASK_APP=server
# $ export FLASK_ENV=development
# $ flask run

from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello():
    return send_from_directory('public', 'index.html')