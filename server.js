var garbageCount = 0;
var recycleCount = 0;
var compostCount = 0;

const express = require('express');
const app = express();
var bodyParser = require('body-parser');

var port = 3000;

var sqlite3 = require('sqlite3').verbose(); // why verbose
var db = new sqlite3.Database('Scores.db');

app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended:true}));

app.use(express.static('./public'));  // this sends clientside files


// setting up server
app.listen(port, function(){
    console.log("Express app listening on port " + port);
});

var requestController = require('./Controllers/request-controller');

app.post('/api/request',requestController.request);

app.get('/api/getStats', function(request, response) {
  response.send({"garbage": garbageCount, "recycle": recycleCount, "compost": compostCount});
});




module.exports.incGarbage = function() {
  console.log("garbage increment");
  garbageCount ++;
}
//module.exports.incGarbage = incGarbage;


module.exports.incRecycle = function() {
    console.log("recycle increment");
  recycleCount ++;
}
//module.exports.incRecycle = incRecycle;

module.exports.incCompost = function() {
    console.log("compost increment");
  compostCount ++;
}
//module.exports.incCompost = incCompost;
