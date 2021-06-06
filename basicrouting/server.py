# run the following in your terminal for django:
# $ django-admin startproject config .
# that will generate the scaffolding for a standard project

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'