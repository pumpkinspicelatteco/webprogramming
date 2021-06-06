// run the following commands in your terminal:
// npm init
// npm i express
// npm start
var express = require('express');
var app = express();

app.get('/', (req, res) => {
    console.log(req);
    res.send('Hello, world!');
});

app.listen(3000, () => {
    console.log('Listening on port 3000!');
});