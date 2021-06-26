// run the following commands in your terminal:
// npm init
// npm i express cors compression spdy serve-favicon
// npm start

// to deploy to heroku
// $ git init
// $ heroku login
// $ heroku git:remote -a <heroku app>
// $ git add -A
// $ git commit -am "feat: add files"
// $ git push heroku master

var compression = require('compression');
var favicon = require('serve-favicon');
var cors = require('cors');
var spdy = require('spdy');

var express = require('express');
var app = express();

app.use(cors());
app.use(compression());
app.use(express.static('./public'));
app.use(favicon('./public/favicon.ico'));

app.get('/hello/world', (req, res) => {
    res.sendFile('index.html', {
        root: './public'
    });
});

// app.listen(3000, () => {
//     console.log('Listening on port 3000!');
// });

const options = {
  spdy: {
    protocols: [ 'h2', 'spdy/3.1', 'http/1.1' ],
    plain: true,
    'x-forwarded-for': true,
    connection: {
      autoSpdy31: false
    }
  }
};
  
const server = spdy.createServer(options, app);
const port = process.env.PORT || 3000;

server.listen(port, (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('Server running at http://localhost:' + port + '/');
  }
});