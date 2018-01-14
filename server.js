const express = require('express');
const app = express();
var bodyParser = require('body-parser');

var port = 3000;

var sqlite3 = require('sqlite3').verbose(); // why verbose
var db = new sqlite3.Database('Scores.db');

app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended:true}));

// setting up server
app.listen(port, function(){
    console.log("Express app listening on port " + port);
});

var requestController = require('./Controllers/request-controller');

app.post('/api/request',requestController.request);