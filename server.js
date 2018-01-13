const express = require('express');
const app = express();
var bodyParser = require('body-parser');

var port = 3000;

var sqlite3 = require('sqlite3').verbose(); // why verbose
var db = new sqlite3.Database('Scores.db');

app.use(bodyParser.json());

// setting up server
app.listen(port, function(){
    console.log("Express app listening on port " + port);
});
