// run the following commands in your terminal:
// npm init
// npm i express
// npm start
var express = require('express');
var app = express();

app.use(express.static('public'));

app.get('/hello/world', (req, res) => {
    res.sendFile('index.html', {
        root: './public'
    });
});

app.listen(3000, () => {
    console.log('Listening on port 3000!');
});