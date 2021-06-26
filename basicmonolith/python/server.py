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

# to enable cors:
# $ pip3 install -U flask-cors

# to enable spdy & h2 we need to upgrade to quart:
# $ pip3 install -U quart quart_cors
# $ export QUART_APP=server:app

# to enable gzip compression:
# $ pip3 install -U quart-compress

# to deploy to heroku
# $ git init
# $ heroku login
# $ heroku git:remote -a <heroku app>
# $ git add -A
# $ git commit -am "feat: add files"
# $ git push heroku master
# $ heroku ps:scale web=1

import os
from quart import Quart, send_from_directory

from quart_cors import cors
from quart_compress import Compress

app = Quart(__name__)
Compress(app)

app = cors(app)

@app.route('/')
async def home():
    return await send_from_directory('./public', 'index.html')

@app.route('/<file>')
async def others(file):
    return await send_from_directory('./public', file)

port = int(os.environ.get('PORT', 5000))
app.run(port=port)